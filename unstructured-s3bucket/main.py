from src.extract_from_s3 import extract_text_from_s3pdf,list_pdf_keys
from src.parse_the_resumes import extract_resume_details
from src.load_to_ssms import create_resume_table,insert_resume_data
from src.utils import move_file_to_archive
#extract listof files in folder
keys=list_pdf_keys("buckettask15","resumes/")
print(keys)
create_resume_table()
#extract the text from the every file
for key in keys:
    
        text=extract_text_from_s3pdf("buckettask15",key)
        details=extract_resume_details(text)
        for k,v in details.items():
                print(f"{k}: {v}")
        insert_resume_data(details)
        move_file_to_archive("buckettask15",key,"archive/")

