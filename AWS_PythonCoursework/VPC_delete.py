#This Python Script will delete a VPC.

import boto3

client=boto3.client("ec2")
response=client.delete_vpc(
    VpcId='vpc-0bdbbcba2ae3b5181')
    
print(response)