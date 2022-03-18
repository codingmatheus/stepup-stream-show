import boto3
import json
import sys
import uuid
import datetime
import random
import os
from botocore.exceptions import ClientError

client = boto3.client("s3")

def is_bucket_empty(bucketName):

    objectKeys = client.list_objects_v2(Bucket=bucketName, MaxKeys=1)
    return "Contents" not in objectKeys or len(objectKeys["Contents"]) <= 0

def populate_screenplays_bucket(bucketName, generateCount):
    
    if( (bucketName is None or bucketName == "") or (generateCount is None or generateCount <= 0)):
        raise Exception(f"Cannot generate screenplays because of missing parameters. bucket: {bucketName}, generateCount: {generateCount}")

    root = "movies/"
    #desired path format: movies/[year]/[genre]/[title]/[screenplayid]/[screenplayfilename]
    try:
        for i in range(generateCount):
            sys.stdout.write('\r')
            progress = round((i + 1 / generateCount) * 100)
            sys.stdout.write(f'Progress: {progress} %' )
            sys.stdout.flush()
            movie_year = random.randint(1900, datetime.datetime.now().year)
            genre = random.choice(["drama","horror","romance","adventure","animation","action"])
            screenplay_file = f'fakescreenplay - {random.choice(["U", "PG", "12A","12","15","18"])}-rated.txt'
            currentScriptPath = os.getcwd()
            upload_file(f'{currentScriptPath}/screenplays/{screenplay_file}', bucketName, f'movies/{movie_year}/{genre}/Title {i}/{uuid.uuid4()}/{screenplay_file}')
    except ClientError as e:
        print(e)
        return False

    sys.stdout.write("\n")

    return True

def upload_file(file_name, bucket, objectPath = None):
    objectPath = file_name if objectPath is None else objectPath

    try:
        client.upload_file(file_name, bucket, objectPath)
    except ClientError as e:
        print(e)
        return False

    return True

if __name__ == "__main__":

    if len(sys.argv) <= 2:
            raise Exception("You must enter the bucket name where you want to upload screenplays to and the amount of screenplays that you want to create.")

 
    bucketName = sys.argv[1]
    generateCount = int(sys.argv[2])

    #bucketName = json.loads(sys.argv[1])
    #bucketName = bucketDetails["StackResourceDetail"]["PhysicalResourceId"]
    
    # if not is_bucket_empty(bucketName):
    #     print("Bucket has already been seeded. No action taken.")
    #     exit()

    result = populate_screenplays_bucket(bucketName, generateCount)

    print(f'Screenplays bucket created and populated? {result}')
