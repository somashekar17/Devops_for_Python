import boto3

s3 = boto3.resource('s3')

def download_from_bucket(s3,file_name,bucket_name,key_name):
    print("Downloading file from S3")
    s3.Bucket(bucket_name).download_file(key_name, file_name)
    print("File downloaded from S3")
#this will download the mentioned image or file from aws .
download_from_bucket(s3,"Quantum It assignment.jpg", "test-bucket-17738", "Quantum It assignment.jpg")