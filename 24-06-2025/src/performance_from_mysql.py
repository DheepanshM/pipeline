import configparser
import urllib.parse
from sqlalchemy import create_engine, text
import pandas as pd

def performance():
             
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



            query1='''select customer_id,count(order_id) as total_sales ,sum(order_amount) as total_revenue
            from orders
            where order_status='Completed'
            group by customer_id
            order by total_revenue desc'''

            perform_table=pd.read_sql_query(query1,con=engine)
            return perform_table