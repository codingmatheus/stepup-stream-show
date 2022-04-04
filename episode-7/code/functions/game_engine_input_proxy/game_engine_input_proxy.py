import boto3
import os
import json

#clients
sfnClient = boto3.client("stepfunctions")
dynamoClient = boto3.client("dynamodb")

#environment vars
GAME_ENGINE_ARN = os.environ["GAME_ENGINE_ARN"]
GAME_STATE_TABLE = os.environ["GAME_STATE_TABLE_NAME"]

def get_latest_game_state():
    item =  dynamoClient.get_item(
        TableName=GAME_STATE_TABLE,
        Key={
            "id": {"S": "guimathed"}
        }
    )
    
    gameStateItem = item["Item"] if "Item" in item else None
    
    if gameStateItem == None:
        return None
    
    print (f'gameStateItem: {gameStateItem}')
    
    gameState =  {
        "TaskToken": gameStateItem["TaskToken"]["S"],
        "Text": gameStateItem["text"]["S"],
        "Options": gameStateItem["options"]["S"]
    }
    
    return gameState
    

def lambda_handler(event, context):
    
    #get game state
    gameState = get_latest_game_state()
    
    newGame = gameState == None

    if newGame:
        execution = sfnClient.start_execution(
            stateMachineArn= GAME_ENGINE_ARN
        )
    else:
        taskToken = gameState["TaskToken"]
        execution = sfnClient.send_task_success(
                taskToken = taskToken,
                output=json.dumps({"choice":"talk_to_woman"})
            )
        
    #read updated gamestate
    updatedGameState = get_latest_game_state()
    
    return updatedGameState