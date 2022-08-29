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

# Driver function
if __name__ == '__main__':
    required="\033[1;3m(Required)\033[0m"
    BUCKET_NAME= input(f"Enter unique bucket name {required}: ")
    delete_bucket(bucket_name=BUCKET_NAME)
