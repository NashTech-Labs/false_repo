import boto3
import botocore
import logging

def delete_bucket(bucket_name):
    """This function deletes all the buckets from s3 bucket

    :param bucket_name: Bucket to create
    :return: True if bucket created, else False
    """
    try:
        s3_client = boto3.client('s3')
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"{bucket_name} is deleted.")
    except botocore.exceptions.ClientError as error:
        logging.error(error)
        return False
    return True


if __name__ == '__main__':
    print("List Delete") 
    BUCKET_NAME= input("Enter unique bucket name: ")
    # REGION= input("Enter region for your Bucket: ")
    delete_bucket(bucket_name=BUCKET_NAME) # region=REGION)
