import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            #url = "localhost"  # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://neighborappadmin:7edbn0aYb6iL7Tc93VWOuJ7794xSsbQXaLxxWqf7HacJHaSFh93vwpNoteoYI5c3ULm2JxnW6NRn0hW0hH4XeQ==@neighborappadmin.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighborappadmin@"
            client = pymongo.MongoClient(url)
            database = client['neighborapp']
            collection = database['advertisementsCol']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )