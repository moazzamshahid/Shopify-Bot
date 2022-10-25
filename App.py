from pymongo import MongoClient
from pymongo.errors import OperationFailure
from bot_function import Bot
import json

def Database():
    client = MongoClient('mongodb+srv://bot123:bot123@cluster0.87qvcox.mongodb.net/?retryWrites=true&w=majority')
    db = client.get_database('supplementSellingDB')
    records = db.businessSetting
    return list(records.find())
def Credentials():
    f = open('credentials.json')
    return json.load(f)



if __name__=="__main__":
    while True:
        request_data = Database()
        credentials=Credentials()
        for data in request_data:
            print(data)
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
            else:
                Bot(username=credentials["username"],
                password=credentials["password"],
                name=request_data["name"].strip(),
                country=data["country"].strip(),
                zip=data["zip"].strip(),
                city=data["city"].strip(),
                address=data["address"].strip()
                )
             
            
        
            









