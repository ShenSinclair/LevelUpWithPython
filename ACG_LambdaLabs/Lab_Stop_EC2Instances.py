import boto3

def lambda_handler(event, context):
    
    #Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
                for region in ec2_client.describe_regions()['Regions']]
    #Iterate over each region
    for region in regions:
        ec2=boto3.resource('ec2', region_name = region)
        print("Region", region)
        
        #Get only running instances
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        #Stop the instances
        for instance in instances:
            instance.stop()
            print('Stopped instances: ', instance.id)
            
#Make sure to create EventBridge Event to schedule CRON timeout
#update configuration timeout for Fx
#Create Lambdafx Role with Lab execution role