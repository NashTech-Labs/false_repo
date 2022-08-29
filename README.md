# Basic_s3_bucket_operation_using_boto3

This repository contains scripts to perform basic S3 bucket oprations like list S3 buckets, create a S3 bucket, delete a S3 bucket. It also include a file which have all these operation combined.



-------------

**Files:** 
```
      1. allBucketOperationInOne.py
      2. createS3Bucket.py
      3. deleteS3Bucket.py
      4. listAndCountBuckets.py
```

## How to run the above scripts

1. First configure the aws credentials on whatever machine you want to run the script by running the below command.

    The profile name in the below configuration will be used in the script and the region should be same wherever the instance is running

    ```
    aws configure
    ```

2. Now, from the current directory run the following command according to your need. Please update your bucket variables before use.

    ```
    # All bucket opration in one
      python3  allBucketOperationInOne.py

    # To create a S3 bucket
      python3 createS3Bucket.py

    # To delete a s3 bucket
      python3 deleteS3Bucket.py

    # To list all buckets
      python3 listAndCountBuckets.py
    ```