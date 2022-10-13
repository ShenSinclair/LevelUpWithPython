import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-026b57f3c383c2eec",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ApacheWebServerKey",
        SubnetId="subnet-0e8027bdf19b9e9e2")
        
print(instances)