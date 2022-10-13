import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-026b57f3c383c2eec",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="Key_Pair_Name",
        SubnetId="subnet-0e8027bdf19b9e9e2")
#to launch multiple instances change Min & Max Count to a number > 1. 
print(instances)