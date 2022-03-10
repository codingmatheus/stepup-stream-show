import boto3
import json
import sys
import uuid
import datetime
import random
import os
from botocore.exceptions import ClientError

client = boto3.client("s3")

def populate_movies_bucket(bucketName):
    root = "movies/"
    #desired path format: movies/[year]/[genre]/[title]/[scriptid]/[scriptfilename]
    try:
        for i in range(1001):
            sys.stdout.write('\r')
            progress = round((i / 1001) * 100)
            sys.stdout.write(f'Progress: {progress} %' )
            sys.stdout.flush()
            movie_year = random.randint(1900, datetime.datetime.now().year)
            genre = random.choice(["drama","horror","romance","adventure","animation","action"])
            currentScriptPath = os.getcwd()
            upload_file(f'{currentScriptPath}/seed/fakescreenplay.txt', bucketName, f'/movies/{movie_year}/{genre}/Title {i}/{uuid.uuid4()}/fakescreenplay.txt')
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

    if len(sys.argv) <= 1:
            raise Exception("You must enter the bucket name that stores all the movie scripts.")

    bucketDetails = json.loads(sys.argv[1])
    bucketName = bucketDetails["StackResourceDetail"]["PhysicalResourceId"]
    
    result = populate_movies_bucket(bucketName)

    print(f'Movie scripts bucket created and populated? {result}')
