import configparser
import urllib.parse
from sqlalchemy import create_engine, text
import pandas as pd
def extract_table(table_name:str):
        config = configparser.ConfigParser()
        config.read(r'C:\Users\Dheepansh\Documents\python_tutorial\config.ini')
        
        username = config['MySQL']['username']
        password = config['MySQL']['password']
        host     = config['MySQL']['host']
        database = config['MySQL']['database']
        driver   = config['MySQL']['driver']
        
        encoded_password = urllib.parse.quote_plus(password)
        
        connection_string = f"mysql+{driver}://{username}:{encoded_password}@{host}/{database}"
        engine = create_engine(connection_string)
        
        
        #fetch orders table from mysql
        fetched_order_table = pd.read_sql_table(table_name,con=engine)
        
        return fetched_order_table
        
 