import configparser
import urllib.parse
from sqlalchemy import create_engine
import pandas as pd
def load_data(data):
        #read the config
        
        config = configparser.ConfigParser()
        config.read(r'C:\Users\Dheepansh\Documents\python_tutorial\config.ini')

        #load credentials
        username = config['Sql']['username']
        password = config['Sql']['password']
        server     = config['Sql']['server']
        database = config['Sql']['database']
        driver   = config['Sql']['driver']

        params = urllib.parse.quote_plus(
            f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        )
        
        engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

        send_the_data=data
        send_the_data.to_sql(name='orders_from_mysql',con=engine,index=False,if_exists='replace')


