sam build | grep "Failed" &> /dev/null

if [ $? == 1 ]; then
    sam deploy
fi

movie_scripts_bucket=$(aws cloudformation describe-stack-resource --stack-name sfndemo-s3pagination --logical-resource-id MovieScriptsBucket)
python3 seed/seed_movie_scripts_bucket.py "$movie_scripts_bucket"

