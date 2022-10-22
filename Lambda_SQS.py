import json
import boto3

from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    sqs = boto3.client('sqs')
    
    sqs.send_message(QueueUrl ="https://sqs.us-east-1.amazonaws.com/618548866628/sheniellwk15project", MessageBody = date_time)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }
