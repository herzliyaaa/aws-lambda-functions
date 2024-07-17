import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client("ec2", region_name="<region>")
sns = boto3.client("sns", region_name="<region>")
s3 = boto3.client("s3", region_name="<region>")

instance_id = "<your-instance-id>"
sns_topic_arn = "<sns-topic-arn>"
bucket_name = "<s3-bucket-name>"
ip_file_key = "ec2_ip_address.txt"


def lambda_handler(event, context):
    response = ec2.describe_instances(InstanceIds=[instance_id])
    ip_address = response["Reservations"][0]["Instances"][0]["PublicIpAddress"]
    logger.info(f"Current IP address: {ip_address}")
    previous_ip = get_previous_ip()
    logger.info(f"Previous IP address: {previous_ip}")

    if ip_address != previous_ip:
        message = (
            f"The IP address of EC2 instance {instance_id} has changed to {ip_address}."
        )
        sns.publish(
            TopicArn=sns_topic_arn, Message=message, Subject="EC2 IP Address Change"
        )
        save_new_ip(ip_address)
        logger.info("IP address changed. Notification sent.")


def get_previous_ip():
    try:
        response = s3.get_object(Bucket=bucket_name, Key=ip_file_key)
        previous_ip = response["Body"].read().decode("utf-8")
        return previous_ip
    except s3.exceptions.NoSuchKey:
        logger.info("No previous IP address found.")
        return None


def save_new_ip(ip_address):
    s3.put_object(Bucket=bucket_name, Key=ip_file_key, Body=ip_address)
    logger.info("New IP address saved.")
