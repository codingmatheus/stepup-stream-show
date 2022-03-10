const AWS = require("aws-sdk")
const dynamodb = new AWS.DynamoDB()
const tableName = process.env.TABLE_NAME

exports.handler = async (event) => {
    
    if(event.MovieDataPath == null)
        {
            throw new Error("MovieDataPath was not provided.")
        }

    const movieInfo = event.MovieDataPath.split("/")
    
    const id = movieInfo[4]
    const title = movieInfo[3]
    
    var params = {
        TableName: tableName,
        Item: {
            "id": {"S": id},
            "title": {"S": title},
            "screenplay": {"S": event.MovieDataPath }
        }
    }
    
    var result = await dynamodb.putItem(params, function(err, data){
       if(err) console.log(err, err.stack)
       else console.log("success", data)
    }).promise();
    
    
};
