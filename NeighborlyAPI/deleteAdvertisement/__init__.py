import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            #url = "localhost"  # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://neighborappadmin:7edbn0aYb6iL7Tc93VWOuJ7794xSsbQXaLxxWqf7HacJHaSFh93vwpNoteoYI5c3ULm2JxnW6NRn0hW0hH4XeQ==@neighborappadmin.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighborappadmin@"
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
