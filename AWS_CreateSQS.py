import boto3

sqs = boto3.resource('sqs')

response = sqs.create_queue(QueueName='sheniellwk15project')

print(response.url)
