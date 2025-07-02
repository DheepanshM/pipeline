from src.extract_from_mongodb import extract_data
from src.transform import transform_data
from src.load_to_dynamodb import load_data
from src.connect_to_dynamo_db import get_dynamo_resource

mongo_uri="mongodb://localhost:27017/"
db_name="pipelines"
#collection_name="project_task" #for semi structured data
#table_name="project_table" #for semi structured data
collection_name="project_task_unstructured" #for unstructured data
table_name="doc_unstructured" # for unstructured_data


documents=extract_data(mongo_uri,db_name,collection_name)
transformed_docs=transform_data(documents)

dynamodb=get_dynamo_resource()
table=dynamodb.Table(table_name)
load_data(transformed_docs, table)

print("ETL complete: MongoDB → DynamoDB")
