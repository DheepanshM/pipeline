from src.extract_from_dynamo import extract_from_dynamo
from src.transform import transform_dynamic
from src.load_to_sql import load_to_sql
import pandas as pd

# dynamo_data=extract_from_dynamo("project_table")# for semi structured

# df=transform_data(dynamo_data) #for semi structured

# load_to_sql(df,"sql_table_from_dynamodb")#for semi structured
#the below code for unstructured
dynamo_data=extract_from_dynamo("doc_unstructured")
df = transform_dynamic(pd.DataFrame(dynamo_data))


load_to_sql(df['projects'], "projects")
load_to_sql(df['technologies'], "project_technologies")
load_to_sql(df['milestones'], "project_milestones")
load_to_sql(df['team_members'], "project_team_members")
