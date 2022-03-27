# Build and deploy the stack used in episode 2 of the Step UP! twitch show on the AWS channel titled "How to handle AWS Step Functions data size limits when working with Amazon DynamoDB"
# ATTENTION: this will build a simple stack consisting of 1 AWS Step Functions's workflow, 1 AWS Simple Queue Service's queue and 1 Amazon DynamoDB and will incur a small cost on your AWS account.
# REQUIREMENTS: you must have AWS SAM and Python 3.x installed

sam build
sam deploy
