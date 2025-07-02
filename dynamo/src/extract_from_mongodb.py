from pymongo import MongoClient

def extract_data(mongo_uri:str,db_name:str,collection_name:str):
    client=MongoClient(mongo_uri)
    db=client[db_name]
    collection=db[collection_name]
    documents=list(collection.find())

    return documents

