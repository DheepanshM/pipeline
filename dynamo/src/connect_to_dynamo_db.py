import configparser
import boto3

def get_dynamo_resource():
    config=configparser.ConfigParser()
    config.read("config.ini")

    return boto3.resource(
        'dynamodb',
        region_name=config["aws"]["region_name"],
        aws_access_key_id=config["aws"]["aws_access_key_id"],
        aws_secret_access_key=config["aws"]["aws_secret_access_key"]
    )
    