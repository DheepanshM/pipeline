import configparser
import urllib.parse
from sqlalchemy import create_engine
import pandas as pd

def get_engine():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Dheepansh\Documents\python_tutorial\config.ini')

    username = config['Sql']['username']
    password = config['Sql']['password']
    server   = config['Sql']['server']
    database = config['Sql']['database']
    driver   = config['Sql']['driver']

    params = urllib.parse.quote_plus(
        f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    )
    return create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

def load_to_ssms(df_dict: dict, if_exists='replace'):
    
    engine = get_engine()

    for table_name, df in df_dict.items():
        if not df.empty:
            df.to_sql(name=table_name, con=engine, if_exists=if_exists, index=False)
            print(f"Loaded {len(df)} rows into '{table_name}' table.")
        else:
            print(f"Skipping empty table: {table_name}")

