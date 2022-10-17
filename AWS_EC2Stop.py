#Import boto3
import boto3
from time import sleep

#List of EC2 instance IDs
Ids=['i-0e89635f54705fc9f','i-028a5a2a44770a26d','i-0f4cc45b5139f705b']

#Resource variable setting
ec2 = boto3.resource("ec2")

#Instance termination
x = ec2.instances.filter(InstanceIds=Ids).stop()

#Display in terminal
print("Stopping...")
sleep(10)
print(x)
