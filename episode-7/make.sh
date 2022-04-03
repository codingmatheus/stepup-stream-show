sam build | grep "Failed" &> /dev/null

if [ $? == 1 ]; then
    sam deploy
fi