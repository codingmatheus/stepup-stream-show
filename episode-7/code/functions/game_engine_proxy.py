import boto3
import os
import json

#clients
sfnClient = boto3.client("stepfunctions")

#environment vars
GAME_ENGINE_ARN = os.environ["GAME_ENGINE_ARN"]

def lambda_handler(event, context):

    execution = sfnClient.start_execution(
        stateMachineArn= GAME_ENGINE_ARN
    )
    
    response = sfnClient.describe_execution(
        executionArn=execution["executionArn"]
        )
        
    return json.loads(response["output"])