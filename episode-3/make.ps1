# DESCRIPTION: Build and deploy the stack used in episode 3 of the Step UP! twitch show on the AWS channel titled "Handling Amazon S3 pagination with AWS Step Functions"
# ATTENTION: This will build a stack on your AWS account and you will be charged for usage. 
#            Please make sure to tear down the resources after playing with the demo to stop incurring charges. 
#            You can easily tear all resources down by going into CloudFormation and choosing to delete the whole stack.
# REQUIREMENTS: you must have AWS SAM and Python 3.x installed

sam build
sam deploy
$bucket_details= aws cloudformation describe-stack-resource --stack-name sfndemo-dynamodb-largeitem --logical-resource-id SFNDemoDynamoDBLargeItem | Out-String
$bucket_details = $bucket_details.Replace("""", "\""")
python ./seed/seed_movie_scripts_bucket.py $bucket_details