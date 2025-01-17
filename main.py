import boto3

# Initialize the S3 resource
s3 = boto3.resource('s3')

# Define bucket and file details
bucket_name = 'my-bucket'
source_key = 'uploads/file1.csv'
destination_key = 'processed/file1.csv'

# Move the file by copying and deleting the original
s3.Object(bucket_name, destination_key).copy_from(CopySource={'Bucket': bucket_name, 'Key': source_key})
s3.Object(bucket_name, source_key).delete()

print(f"File moved from {source_key} to {destination_key}")
