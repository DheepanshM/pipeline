import boto3
#io for to treat bytes or strings like file objects
import io
#PDF2 to read pdf file
from PyPDF2 import PdfReader
import configparser

def extract_text_from_s3pdf(bucket_name,key):
    #to get credentials
    config=configparser.ConfigParser()
    config.read(r'C:\Users\Dheepansh\Documents\python_tutorial\config.ini')

    aws_access_key_id = config['aws']['aws_access_key_id']
    aws_secret_access_key = config['aws']['aws_secret_access_key']
    region = config['aws'].get('region', 'us-east-1')
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region
    )
    #to get pdf from s3
    response = s3.get_object(Bucket=bucket_name, Key=key)
    #to read raw binary content 
    pdf_bytes=response['Body'].read()
    #byte data to file object to read
    reader = PdfReader(io.BytesIO(pdf_bytes))
    text=""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def list_pdf_keys(bucket_name,prefix):

    config=configparser.ConfigParser()
    config.read(r'C:\Users\Dheepansh\Documents\python_tutorial\config.ini')

    aws_access_key_id = config['aws']['aws_access_key_id']
    aws_secret_access_key = config['aws']['aws_secret_access_key']
    region = config['aws'].get('region', 'us-east-1')
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region
    )
    response = s3.list_objects_v2(Bucket=bucket_name,Prefix=prefix)

    keys=[]
    for item in response.get("Contents",[]):
        file_name=item['Key']

        if file_name.endswith('.pdf'):
            keys.append(file_name) #add to list

    return keys


