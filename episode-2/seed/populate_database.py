import boto3
import json
import sys

dynamodb = boto3.resource("dynamodb")

def load_movies_data():
    with open("seed/data/movies.json") as movies_file:
        movies = json.load(movies_file)
        return movies


def populate_db(movies, table_name):
    table = dynamodb.Table(table_name)

    existing_item = table.get_item(Key={"id":"1"}, ProjectionExpression="id")
    if "Item" in existing_item:
       raise Exception(f'Table {table_name} is not empty. Please make sure you using the correct table and delete all items from it before running this script.')
    

    for movie in movies:
        table.put_item(Item=movie)

if __name__ == '__main__':

    if len(sys.argv) <= 1:
        raise Exception("You must enter the name of the Amazon DynamoDB table that you would like to populate with the demo data.")
   
    table_details = json.loads(sys.argv[1])
    

    table_name = table_details["StackResourceDetail"]["PhysicalResourceId"]

    
    movies = load_movies_data()
    populate_db(movies, table_name)

print(f"Successfully populated the Amazon DynamoDB table called {table_name} with the large item demo data.")


    