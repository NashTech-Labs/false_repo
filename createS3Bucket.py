import boto3
import botocore
import logging


def createBucket(bucketName, region):
    """This function creates an S3 bucket in a specified region
    
    :param bucketName: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucketName,
                                CreateBucketConfiguration=location)
        print(f"{bucketName} is created.")
    except botocore.exceptions.ClientError as error: 
        logging.error(error)
        return False
    return True

# Driver function
if __name__ == '__main__':
    required="\033[1;3m(Required)\033[0m"
    optional="\033[1;3m(Optional)\033[0m"
    # Get the bucket name and region
    BUCKET_NAME= input(f"Enter unique bucket name {required}: ")
    REGION= input(f"Enter region for your bucket {required}: ")
    createBucket(BUCKET_NAME, region=REGION)
