# Working with AWS S3 Bucket

## What is S3 Bucket?

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. It allows you to store and retrieve any amount of data from anywhere on the web.

## How to Create an S3 Bucket in AWS

To create an S3 bucket in AWS with the name "aws-s3", follow these step-by-step instructions:

1. Log in to the AWS Management Console.
2. Navigate to the S3 service.
3. Click on the "Create bucket" button.
4. Enter the bucket name as "aws-s3".
5. Choose the region for your bucket.
6. Configure bucket properties and permissions as needed.
7. Click on the "Create bucket" button to create the bucket.

## Python Code to Access S3 Bucket Objects

[Python File](./python.py)

## Prerequisites

Check [Requirements File](./requirements.txt) file 

- [boto3](https://github.com/boto/boto3) module installed.
- Python version 3.x installed.

## IAM User Creation

To create an IAM user in AWS, follow these steps:

1. Log in to the AWS Management Console.
2. Navigate to the IAM service.
3. Click on "Users" in the sidebar.
4. Click on the "Add user" button.
5. Enter the username and select the access type (programmatic access, console access, or both).
6. Set permissions for the user.
7. Review and create the user.


## Create a GitHub Secret for IAM Access Key and Secret

To securely store IAM access keys and secrets in GitHub, follow these steps:

1. Go to your GitHub repository.
2. Navigate to the "Settings" tab.
3. Click on "Secrets" in the sidebar.
4. Click on "New repository secret" and add your IAM access key ID and secret access key as separate secrets.

## How to Execute a Python File

To execute a Python file, you can run it using the Python interpreter. Open a terminal or command prompt, navigate to the directory containing the Python file, and run the following command:

```bash
python3 python.py
```
