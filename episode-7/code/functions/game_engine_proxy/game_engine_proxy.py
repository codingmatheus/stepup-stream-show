import boto3
import os
import json
import datetime
import time
import uuid

#clients
sfnClient = boto3.client("stepfunctions")
dynamoClient = boto3.client("dynamodb")

#environment vars
GAME_ENGINE_ARN = os.environ["GAME_ENGINE_ARN"]
GAME_STATE_TABLE = os.environ["GAME_STATE_TABLE_NAME"]


def lambda_handler(event, context):
    
    username = event["username"]
    taskToken = event["taskToken"]
    gameId = event["gameId"] if "gameId" in event else None
    newGame = True if (gameId is None or gameId == "") else False
    
    newTurnId = str(uuid.uuid4())
    turnPlayedDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if newGame:
        gameId = str(uuid.uuid4())
        execution = sfnClient.start_execution(
            stateMachineArn= GAME_ENGINE_ARN,
            input=json.dumps({"username": username, "gameId": gameId, "turnId": newTurnId, "turnPlayedDate": turnPlayedDate})
        )
    else:
        choice = event["choice"]
        execution = sfnClient.send_task_success(
                taskToken = taskToken,
                output=json.dumps({"username": username, "gameId": gameId, "choice": choice, "turnId": newTurnId, "turnPlayedDate": turnPlayedDate})
            )
    
    time.sleep(1)
    updatedGameState = get_latest_game_state(username, gameId, newTurnId)
    
    return updatedGameState
    
def get_latest_game_state(username, gameId, turnId):

    print(username + " " + gameId + " " + turnId)
    
    queryResult =  dynamoClient.query(
        TableName=GAME_STATE_TABLE,
        KeyConditionExpression="#username = :username AND #gameId = :gameId",
        FilterExpression="#turnId = :turnId",
        ExpressionAttributeNames={"#username": "username", "#gameId": "gameId", "#turnId": "turnId"},
        ExpressionAttributeValues={":username": {"S": username}, ":gameId": {"S": gameId}, ":turnId": {"S": turnId}}
    )
    
    items = queryResult["Items"]
    
    gameStateItem = None if not items else items[0]
    
    if gameStateItem == None:
        return None
    
    gameState =  {
        "TaskToken": gameStateItem["taskToken"]["S"],
        "UserName": gameStateItem["username"]["S"],
        "GameId": gameStateItem["gameId"]["S"],
        "TurnId": gameStateItem["turnId"]["S"],
        "Text": gameStateItem["text"]["S"],
        "Options": gameStateItem["options"]["S"]
    }
    
    return gameState
    
