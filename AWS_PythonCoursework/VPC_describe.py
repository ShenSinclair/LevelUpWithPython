#Python script to describe available VPCs.

import boto3

vpc=boto3.client("ec2")

x=vpc.describe_vpcs()
no_of_vpcs=x["Vpcs"]
print(len(no_of_vpcs))
for vpc in no_of_vpcs:
    print(vpc["VpcId"])