import boto3

s3 = boto3.resource('s3')

#This code will show how many s3 buckets present in my account.
for bucket in s3.buckets.all():
    print(bucket.name)



