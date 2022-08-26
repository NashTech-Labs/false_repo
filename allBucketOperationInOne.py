import boto3
import botocore
import logging

def list_bucket():
    """This function list all the buckets from s3 bucket
    """

    # Retrieve the list of existing buckets
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')   


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
        print(f"{bucket_name} is created.")
        list_bucket()
    except botocore.exceptions.ClientError as error:
        logging.error(error)
        return False
    return True


def delete_bucket(bucket_name):
    """This function deletes all the buckets from s3 bucket

    :param bucket_name: Bucket to create
    :return: True if bucket created, else False
    """
    try:
        s3_client = boto3.client('s3')
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"{bucket_name} is deleted.")
        list_bucket()
    except botocore.exceptions.ClientError as error:
        logging.error(error)
        return False
    return True


if __name__ == '__main__':
    print("Choose your operation:")
    print("\t1. List your bucket")
    print("\t2. Create a bucket")
    print("\t3. Delete a bucket")
    choice=input("Your Choice:")
    if choice=="1":
        print("List Bucket")
        list_bucket()
    elif choice=="2":   
        print("List Create") 
        BUCKET_NAME= input("Enter unique bucket name: ")
        REGION= input("Enter region for your Bucket: ")
        create_bucket(bucket_name=BUCKET_NAME, region=REGION)
    elif choice=="3":
        print("List Delete") 
        BUCKET_NAME= input("Enter unique bucket name: ")
        # REGION= input("Enter region for your Bucket: ")
        delete_bucket(bucket_name=BUCKET_NAME) # region=REGION)
