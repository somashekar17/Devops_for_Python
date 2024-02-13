import boto3

s3 = boto3.resource('s3')

def upload_to_bucket(s3, file_name, bucket_name, key_name):
    print("Uploading file to S3")
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("File uploaded to S3")

# this code will upload the file from local to aws s3 bucket
upload_to_bucket(s3, "C:/Users/nsoma/OneDrive/Pictures/h.jpg", "test-bucket-17738", "h.jpg")
