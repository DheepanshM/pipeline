from sqlalchemy import create_engine
import configparser
import urllib

def load_to_sql(df, table_name):
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

        # Load to SQL Server (append or replace)
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
