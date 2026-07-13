import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client('ec2')

# Replace with your actual Quarantine Security Group ID
QUARANTINE_SG_ID = "sg-09426be043e8281ca"

def lambda_handler(event, context):
    logger.info("GuardDuty event received")
    logger.info(json.dumps(event))

    try:
        # Extract EC2 instance ID from GuardDuty finding
        instance_id = event['detail']['resource']['instanceDetails']['instanceId']
        logger.info(f"Compromised instance identified: {instance_id}")

        # Get current security groups
        response = ec2.describe_instances(InstanceIds=[instance_id])
        network_interface_id = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['NetworkInterfaceId']

        # Apply Quarantine Security Group
        ec2.modify_network_interface_attribute(
            NetworkInterfaceId=network_interface_id,
            Groups=[QUARANTINE_SG_ID]
        )

        # Tag instance as quarantined
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[{'Key': 'Status', 'Value': 'Quarantined'}]
        )

        logger.info("Instance successfully quarantined")

        return {
            'statusCode': 200,
            'body': 'EC2 instance quarantined successfully'
        }

    except Exception as e:
        logger.error(f"Error during remediation: {str(e)}")
        raise e
