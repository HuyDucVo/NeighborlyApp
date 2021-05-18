import azure.functions as func
import pymongo
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            #url = "localhost"  # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://neighborappadmin:7edbn0aYb6iL7Tc93VWOuJ7794xSsbQXaLxxWqf7HacJHaSFh93vwpNoteoYI5c3ULm2JxnW6NRn0hW0hH4XeQ==@neighborappadmin.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighborappadmin@"
            client = pymongo.MongoClient(url)
            database = client['neighborapp']
            collection = database['advertisementsCol']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

