import configparser
import boto3

def move_file_to_archive(bucket_name, source_key, archive_prefix="archive/"):
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

    # New path in archive folder
    dest_key = archive_prefix + source_key.split('/')[-1]

    # Copy original file to archive location
    s3.copy_object(
        Bucket=bucket_name,
        CopySource={'Bucket': bucket_name, 'Key': source_key},
        Key=dest_key
    )

    # Delete original file
    s3.delete_object(Bucket=bucket_name, Key=source_key)

    
