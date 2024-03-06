import boto3
import os
from botocore.exceptions import ClientError

# Specify your AWS credentials (or use IAM role if running on EC2 instance with correct permissions)
# iam_user_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
# iam_user_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

iam_user_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
iam_user_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Specify the AWS region and S3 bucket name
region_name = 'ap-south-1'
bucket_name = 'keerti-y.aws.s3.bucket1'
object_name = 'test-bucket'
file_data = 'keerti Y'


# Create an S3 client
s3 = boto3.client('s3', region_name=region_name, 
                  aws_access_key_id=iam_user_access_key_id, 
                  aws_secret_access_key=iam_user_secret_access_key)

def read_object(bucket_name, key):
    response = s3.get_object(Bucket=bucket_name, Key=key)
    return response['Body'].read().decode('utf-8')

# Write an object to S3
def write_object(bucket_name, key, data):
    s3.put_object(Bucket=bucket_name, Key=key, Body=data.encode('utf-8'))

# List all objects in S3 bucket
def list_objects(bucket_name):
    objects = []
    response = s3.list_objects_v2(Bucket=bucket_name)
    for obj in response.get('Contents', []):
        objects.append(obj['Key'])
    return objects

def append_object(bucket_name, key, data):
    # Read existing object
    response = s3.get_object(Bucket=bucket_name, Key=key)
    existing_data = response['Body'].read().decode('utf-8')
    
    # Append new data to existing data
    updated_data = existing_data + data
    
    # Upload updated data as a new object
    s3.put_object(Bucket=bucket_name, Key=key, Body=updated_data.encode('utf-8'))


#     try:
#         # Check if the object already exists
#         s3.head_object(Bucket=bucket_name, Key=object_name)
#         print(f"Object '{object_name}' already exists in bucket '{bucket_name}'")
#         return object_name
#     except ClientError as e:
#         # If the object does not exist, create it
#         if e.response['Error']['Code'] == '404':
#             s3.put_object(Bucket=bucket_name, Key=object_name)
#             print(f"Object '{object_name}' created in bucket '{bucket_name}'")
#             return object_name
#         else:
#             # If another error occurs, print the error message
#             print("An error occurred:", e.response['Error']['Message'])

def create_s3_object(bucket_name, object_name, object_data):
    # Put the object in the bucket
    try:
        response = s3.put_object(Bucket=bucket_name, Key=object_name, Body=file_data)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"Object '{object_name}' created in bucket '{bucket_name}'")
            return True
    except ClientError as e:
        # Handle the exception
        print(f"An error occurred: {e}")
        return False



# Example usage
if __name__ == "__main__":
    # Read an object
    success = create_s3_object(bucket_name, object_name, file_data)
    if success:
        print("Object creation successful!")
    else:
        print("Object creation failed.")

    print("List of all objects in S3 bucket:")
    all_objects = list_objects(bucket_name)
    for obj in all_objects:
        print(obj)

        # add new data to file 
        new_data = "New data to write to S3"
        write_object(bucket_name, obj, new_data)

        # read object data 
        object_data = read_object(bucket_name, obj)
        print("Read object from S3:")
        print(object_data)

        # append a data to existing file 
        data = "keerti Y"
        append_object(bucket_name,obj,data)

        object_data = read_object(bucket_name, obj)
        print("Read object from S3:")
        print(object_data)

    

 
