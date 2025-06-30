from pymongo import MongoClient
import pandas as pd
def read_data(db_name = 'pipelines',collection_name = 'project_task'):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]
    data = list(collection.find({},{'_id':0})) #to get output in the format of list
    return pd.DataFrame(data)

