from contextlib import nullcontext
import boto3
import os
import uuid
import json

#environment vars
TABLE_NAME_KEY="TABLE_NAME"
SCREENPLAYS_BUCKET = "SCREENPLAYS_BUCKET"
RUDE_WORDS = "RUDE_WORDS"

#clients
dynamo = boto3.client("dynamodb")
s3 = boto3.client("s3")
sfn = boto3.client("stepfunctions")

screenplaysTable = os.environ[TABLE_NAME_KEY]
screenplaysBucketName = os.environ[SCREENPLAYS_BUCKET]

def lambda_handler(event, context):

    for record in event['Records']:
        
        body = json.loads(record["body"])
        
        taskToken = body["TaskToken"]
        screenplayObjectKey = body["Key"]
        rating = body["Rating"]
        
        #get screenplay content
        screenplay = s3.get_object(Bucket=screenplaysBucketName, Key=screenplayObjectKey)["Body"].read().decode("utf-8")

        #censor screenplay
        for rudeWord in RUDE_WORDS:
            screenplay.replace(rudeWord, "***")

        #save censored script
        #path convention: movies/[year]/[genre]/[title]/[screenplayid]/[screenplayfilename]
        screenplay_binary = ' '.join(format(ord(x), 'b') for x in screenplay)
        censored_screenplay_id = str(uuid.uuid4())
      
        original_key_parts = screenplayObjectKey.split("/")
        year = original_key_parts[1]
        genre = original_key_parts[2]
        title = original_key_parts[3]
        original_screenplay_filename = original_key_parts[5]

        censored_screenplay_object_key = f'{original_key_parts[0]}/{year}/{genre}/{title}/{censored_screenplay_id}/[CENSORED] {original_screenplay_filename}'
        s3.put_object(Bucket=screenplaysBucketName, Key=censored_screenplay_object_key, Body=screenplay_binary)

        item = {
            "id": { "S": censored_screenplay_id},
            "title": {"S": title},
            "year":{"S": year},
            "genre": {"S": genre},
            "rating": {"S": rating},
            "screenplay": {"S": censored_screenplay_object_key},
            "isCensored": {"BOOL": True},
            "isLive": {"BOOL": False}
        }

        dynamo.put_item(TableName=screenplaysTable, Item=item)

        result = {
            "id": censored_screenplay_id,
            "censoredScreenplayObjectKey": censored_screenplay_object_key
        }

        #call back stepfunction with success
        sfn.send_task_success(
            taskToken=taskToken,
            output= json.dumps(result)
        )
        
        return result
        
        #note that errors have not been handled. You could notify someone in the case of an error or add it to a dead letter queue for manual troubleshooting



