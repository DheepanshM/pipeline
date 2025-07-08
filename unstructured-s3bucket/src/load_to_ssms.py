import configparser
import urllib.parse
from sqlalchemy import create_engine, text


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

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}", fast_executemany=True)

def create_resume_table():
    query = """
    IF OBJECT_ID('dbo.Resumes', 'U') IS NULL
    BEGIN
        CREATE TABLE dbo.Resumes (
            id INT PRIMARY KEY IDENTITY(1,1),
            full_name NVARCHAR(100),
            email NVARCHAR(100),
            phone NVARCHAR(20),
            skills NVARCHAR(MAX),
            projects NVARCHAR(MAX)
        );
    END
    """
    with engine.begin() as conn:
        conn.execute(text(query))


def insert_resume_data(data: dict):
   
    with engine.begin() as conn:
        
        check_query = text("SELECT COUNT(*) FROM Resumes WHERE full_name = :name")
        result = conn.execute(check_query, {"name": data.get("name")})
        count = result.scalar()

        if count == 0:
           
            insert_query = text("""
                INSERT INTO Resumes (full_name, email, phone, skills, projects)
                VALUES (:full_name, :email, :phone, :skills, :projects)
            """)
            conn.execute(insert_query, {
                "full_name": data.get("name"),
                "email": data.get("email"),
                "phone": data.get("phone"),
                "skills": data.get("skills"),
                "projects": data.get("projects")
            })
            

