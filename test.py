import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

mycol = mydb["customers"]

data = {"Name:":"Name","SRN":"SRN"}
mycol.insert_one(data)

print(mydb.list_collection_names())
