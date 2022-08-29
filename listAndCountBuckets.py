import boto3

def list_bucket():
    """This function list all the buckets from s3 bucket
    """

    # Retrieve the list of existing buckets
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    # Output the bucket names
    count=0
    print('Existing buckets are:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
        count+=1
    print(f"Total number of buckets: {count}")

# Driver function
if __name__ == '__main__':
    list_bucket()