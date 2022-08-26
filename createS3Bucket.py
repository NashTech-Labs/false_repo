import boto3
import botocore
import logging


def createBucket(bucketName, region=None):
    """This function creates an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucketName: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            print("kdjclskd")
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucketName)
        else:
            print("qwedqwe")
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucketName,
                                    CreateBucketConfiguration=location)
    except botocore.exceptions.ClientError as error: 
        logging.error(error)
        return False
    return True


if __name__ == '__main__':

    # Get the bucket name and region
    BUCKET_NAME= input("Enter unique bucket name: ")
    REGION= (input("Enter region for your bucket \033[1;3m(Optional)\033[0m: ") or None)
    createBucket(BUCKET_NAME, region=REGION)
