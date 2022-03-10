# Step Up!

Code samples and demos as featured on the Step Up! show on the official AWS Twitch channel at https://twitch.tv/aws
## Notes

- All SAM templates will have a samconfig.toml file containing defaults for the SAM build and deployment. Feel free to update those parameters to your convenience, however, do not change the stack name as it may be used by other scripts and could break the build and deploy process.

- **All stacks will deploy by defaul to the eu-west-1 (Ireland) region.** You can easily change that in the samconfig.toml file included or, if you are executing the SAM commands yourself, you can use ```sam deploy --guided``` to override it.
## Episodes

### Episode 1 - Getting started with AWS Step Functions
- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)  **Build requirements**
    - AWS SAM CLI installed (instructions: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) **Artifacts**
    - SAM template
        - deploys an AWS Step Functions workflow and an AWS Lambda
- ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Instructions**
    - simply navigate to the episode-1 folder after cloning and run ```sam build``` followed by ```sam deploy```

### Episode 2 - How to handle AWS Step Functions data size quotas when working with Amazon DynamoDB 
- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)  **Build requirements**
    - AWS CLI 2.x installed (instructions: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
    - AWS SAM CLI installed (instructions: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
    - Python 3.x installed (instructions: https://wiki.python.org/moin/BeginnersGuide/Download)
    - Either Bash or Powershell installed 
        - If you're using Linux,  macOS or already using WSL on Windows, then you already have bash. Otherwise see here for instructions on how to install WSL on Windows 10/11: https://docs.microsoft.com/en-us/windows/wsl/install
        - Powershell instructions: https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) **Artifacts**
    - SAM template
        - deploys an AWS Step Functions workflow and an Amazon DynamoDB table
    - python script to populate the Amazon DynamoDB table with demo data
    - bash script to build and deploy all resources and populate the database with one command
    - powershell script with the same purpose as the bash script meant for powershell users

- ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Instructions**
    - navigate to the episode-2 folder after cloning
    - run the make file:
        - if you're using Linux, macOS or WSL then run ```bash ./make.sh```
        - if you're using Powershell then run ```./make.ps1```

### Episode 3 - Handling Amazon S3 pagination with AWS Step Functions
- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)  **Build requirements**
    - AWS CLI 2.x installed (instructions: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
    - AWS SAM CLI installed (instructions: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
    - Python 3.x installed (instructions: https://wiki.python.org/moin/BeginnersGuide/Download)
    - Either Bash or Powershell installed 
        - If you're using Linux,  macOS or already using WSL on Windows, then you already have bash. Otherwise see here for instructions on how to install WSL on Windows 10/11: https://docs.microsoft.com/en-us/windows/wsl/install
        - Powershell instructions: https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) **Artifacts**
    - SAM template
        - deploys an AWS Step Functions workflow, an Amazon S3 bucket, an AWS Lambda and a Amazon DynamoDB table
    - python script to populate the Amazon DynamoDB table with demo data
    - bash script to build and deploy all resources and populate the Amazon S3 bucket with one command
    - powershell script with the same purpose as the bash script meant for powershell users

- ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Instructions**
    - navigate to the episode-2 folder after cloning
    - run the make file:
        - if you're using Linux, macOS or WSL then run ```bash ./make.sh```
        - if you're using Powershell then run ```./make.ps1```