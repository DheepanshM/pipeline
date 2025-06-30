from src.insert_to_mongodb import extract_from_text, load_to_mongoDB
from src.extract import read_data
from src.transform import transform_dynamic
from src.load import load_to_ssms

def main():
    

    # Step 1: Insert raw text to MongoDB
    data = extract_from_text(r"C:\Users\Dheepansh\Downloads\Doc_unstructured_1.txt")
    load_to_mongoDB(data)

    # Step 2: Extract from MongoDB
    raw_df = read_data()

    # Step 3: Transform dynamically
    transformed_tables = transform_dynamic(raw_df)

    # Step 4: Load into SQL Server
    load_to_ssms(transformed_tables)
    
    print(" Done!")

if __name__ == "__main__":
    main()


