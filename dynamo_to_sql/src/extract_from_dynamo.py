import configparser
import boto3

def extract_from_dynamo(table_name):
    config=configparser.ConfigParser()
    config.read("config.ini")

    dynamodb= boto3.resource(
        'dynamodb',
        region_name=config["aws"]["region_name"],
        aws_access_key_id=config["aws"]["aws_access_key_id"],
        aws_secret_access_key=config["aws"]["aws_secret_access_key"]
    )

    table=dynamodb.Table(table_name)
    response=table.scan()
    data=response['Items']

#as data is transferred only 1mb from dynamo to other resource
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    return data