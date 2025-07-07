import configparser
import pandas as pd
from sqlalchemy import create_engine, text

def to_sql():
    # Read config
    config = configparser.ConfigParser()
    config.read("C:/Users/Dheepansh/Documents/python_tutorial/config.ini")

    server = config["Sql"]["server"]
    database = config["Sql"]["database"]
    username = config["Sql"]["username"]
    password = config["Sql"]["password"]

    # Create SQLAlchemy engine
    engine = create_engine(
        f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server",
        fast_executemany=True
    )

    # Create table if it doesn't exist
    with engine.begin() as conn:
        conn.execute(text("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='twitter_sentiment' AND xtype='U')
            CREATE TABLE twitter_sentiment (
                tweet_id BIGINT PRIMARY KEY,
                tweet_text NVARCHAR(MAX),
                created_at DATETIME,
                author_id BIGINT,
                sentiment_score FLOAT,
                sentiment_label VARCHAR(10)
            )
        """))

    # Read and clean CSV
    df = pd.read_csv("tweet_data.csv")
    df = df.drop_duplicates(subset="tweet_id")
    df["created_at"] = pd.to_datetime(df["created_at"], errors='coerce')

    # Bulk insert to SQL Server
    try:
        df.to_sql("twitter_sentiment", engine, if_exists="append", index=False, method="multi")
        print("Data loaded to SQL Server")
    except Exception as e:
        print(f"Error inserting data: {e}")

