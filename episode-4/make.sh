sam build | grep "Failed" &> /dev/null

if [ $? == 1 ]; then
    sam deploy
fi

#screenplays_bucket=$(aws cloudformation describe-stack-resource --stack-name sfndemo-screenplaysprocessor --logical-resource-id ScreenplaysBucket)

#python3 seed/seed_screenplays_bucket.py "$screenplays_bucket"

