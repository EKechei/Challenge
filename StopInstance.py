import boto3
region = 'us-east-1'
instances = ['i-037369fd2589da036', 'i-0db10dc9572df9469']
ec2 = boto3.client('ec2', region_name='us-east-1')

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))