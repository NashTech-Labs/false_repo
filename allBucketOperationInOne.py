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
    count=0
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')  
        count+=1
    print(f"Total number of buckets: {count}") 


def create_bucket(bucket_name, region):
    """This function creates an S3 bucket in a specified region
    
    :param bucketName: Bucket to create
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

    Warning: Make sure bucket is Empty i.e. no object is present in the bucket.
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
        print("List Operation Selected")
        list_bucket()
    elif choice=="2":   
        print("Create Operation Selected") 
        BUCKET_NAME= input("Enter unique bucket name: ")
        REGION= input("Enter region for your Bucket: ")
        create_bucket(bucket_name=BUCKET_NAME, region=REGION)
    elif choice=="3":
        print("Delete Operation Selected") 
        BUCKET_NAME= input("Enter unique bucket name: ")
        # REGION= input("Enter region for your Bucket: ")
        delete_bucket(bucket_name=BUCKET_NAME) # region=REGION)
