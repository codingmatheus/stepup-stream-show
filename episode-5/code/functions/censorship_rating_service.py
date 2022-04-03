import json
import boto3
import os 

#environment vars
RUDE_WORDS = "RUDE_WORDS"

#clients
s3 = boto3.client("s3")

censoredTerms = os.environ[RUDE_WORDS]


def get_censorship_rating(censoredTermsCount):
    
    if censoredTermsCount <= 0:
        return "U"
    elif censoredTermsCount == 1:
        return "PG"
    elif censoredTermsCount == 2:
        return "12A"
    elif censoredTermsCount == 3:
        return "12"
    elif censoredTermsCount == 4:
        return "15"
    else:
        return "18"
    
def lambda_handler(event, context):
    
    if "Bucket" not in event or event["Bucket"] == "":
        raise Exception("Missing parameter or empty value: Bucket")
        
    if "ScreenplayObjectKey" not in event or event["ScreenplayObjectKey"] == "":
        raise Exception("Missing parameter or empty value: ScreenplayObjectKey")
    
    bucketName = event["Bucket"]
    screenplay_key = event["ScreenplayObjectKey"]
    
    screenplay = s3.get_object(Bucket=bucketName, Key=screenplay_key)["Body"].read().decode("utf-8")
    
    censoredTermsCount = 0
    
    for term in censoredTerms:
        if screenplay.find(term) != -1:
            censoredTermsCount = censoredTermsCount + 1;
    
    rating = get_censorship_rating(censoredTermsCount)
    
    return {
        'IsCensored': censoredTermsCount > 0,
        'Rating': rating
    }
