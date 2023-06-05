import boto3
region = 'us-east-1'
instances = ['i-058c934ca37be80b2', 'i-0c6a8b96ce9383b91']
ec2 = boto3.client('ec2', region_name='us-east-1')

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))