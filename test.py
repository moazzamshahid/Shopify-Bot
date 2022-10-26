from App import Database
from bson.objectid import ObjectId

request_data, records = Database()

print(request_data)

id='6336a2c43e043374b6317081'
filter = { '_id': ObjectId('6336a2c43e043374b6317081') }
newvalues = { "$set": { 'store_created': 'yes' } }
records.update_one(filter,newvalues)