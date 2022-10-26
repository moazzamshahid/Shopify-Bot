from pymongo import MongoClient
from pymongo.errors import OperationFailure
from bot_function import Bot
import json
from bson.objectid import ObjectId
def Database():
    client = MongoClient('mongodb+srv://bot123:bot123@cluster0.87qvcox.mongodb.net/?retryWrites=true&w=majority') # This line logins and makes connection to mongodb account
    db = client.get_database('supplementSellingDB') # then it connects to database
    records = db.businessSetting #this line downloads the tables and stores it in record.
    return list(records.find()), records # this line returns the table in list data type. 
def Credentials():
    f = open('credentials.json')
    return json.load(f)



if __name__=="__main__":
    while True:
        request_data, records = Database()
        credentials=Credentials()
        
        for data in request_data:
            print(data)
            if "store_created" not in data:
                if data["state"]:
                    Bot(username=credentials["username"],
                    password=credentials["password"],
                    name=data['name'].strip(),
                    country=data["country"].strip(),
                    state=data["state"].strip(),
                    zip=data["zip"].strip(),
                    city=data["city"].strip(),
                    address=data["address"].strip(),
                    state_check=True
                    )
                    filter = {'_id': data["_id"] }
                    newvalues = { "$set": { 'store_created': 'yes' } }
                    records.update_one(filter,newvalues)
                else:
                    Bot(username=credentials["username"],
                    password=credentials["password"],
                    name=request_data["name"].strip(),
                    country=data["country"].strip(),
                    zip=data["zip"].strip(),
                    city=data["city"].strip(),
                    address=data["address"].strip()
                    )
                    filter = {'_id': data["_id"] }
                    newvalues = { "$set": { 'store_created': 'yes' } }
                    records.update_one(filter,newvalues)
             
            
        
            









