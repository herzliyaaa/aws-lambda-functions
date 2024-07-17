import boto3

ec2 = boto3.client('ec2', region_name='<region>') 
instance_id = '<your-instance-id>'  

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=[instance_id])
    return f'Stopped EC2 instance: {instance_id}'
