movies = []

def populate():
	movies.append({"Title": "Titanic", "Platform": "Netflix"})
	movies.append({"Title": "Titanic", "Platform": "Amazon Prime"})
	movies.append({"Title": "Saw", "Platform": "Netflix"})
	
populate()

def lambda_handler(event, context):
	
	result = []
	
	for movie in movies:
		if movie["Title"] == event["Title"]:
			result.append(movie)
	
	return result