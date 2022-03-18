import boto3
import json

from datetime import datetime

sfn = boto3.client("stepfunctions")

def lambda_handler(event, context):

    if not "TaskToken" in event:
        raise ValueError("Missing parameter: Task Token")

    if not "ScreenplayId" in event:
        raise ValueError("Missing parameter: ScreenplayId")

    if not "ApproverFullName" in event:
        raise ValueError("Missing parameter: ApproverFullName")
    
    if not "IsApproved" in event:
        raise ValueError("Missing parameter: IsApproved")


    taskToken = event["TaskToken"]
    screenplayId = event["ScreenplayId"]
    isApproved = bool(event["IsApproved"])
    approverFullName = event["ApproverFullName"]

    result = {
        "screenplayId": screenplayId,
        "isApproved": isApproved,
        "approverFullName": approverFullName,
        "approvalDate": str(datetime.now())
    }

    sfn.send_task_success(taskToken=taskToken, output=json.dumps(result))
        

