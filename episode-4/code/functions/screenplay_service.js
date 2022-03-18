const AWS = require("aws-sdk")
const dynamodb = new AWS.DynamoDB()
const tableName = process.env.TABLE_NAME

exports.handler = async (event) => {
    
    if(event.ScreenplayObjectKey == null)
        {
            throw new Error("ScreenplayObjectKey was not provided.")
        }
    
        if(event.Rating == null)
        {
            throw new Error("Rating was not provided.")
        }

    const movieInfo = event.ScreenplayObjectKey.split("/")
    
    const title = movieInfo[4]
    const id = movieInfo[5]
    const rating = event.Rating

    var params = {
        TableName: tableName,
        Item: {
            "id": {"S": id},
            "title": {"S": title},
            "rating": {"S": rating},
            "screenplay": {"S": event.ScreenplayObjectKey },
            "isCensored": {"BOOL": false},
            "isLive": {"BOOL": false}
        }
    }
    
    await dynamodb.putItem(params, function(err, data){
       if(err) console.log(err, err.stack)
       else console.log("success", data)
    }).promise();

    const result = {
        id: id
    }

    return result
    
    
};