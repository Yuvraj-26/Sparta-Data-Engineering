import boto3
import pprint as pp
import json
import pandas as pd
import io

s3_client = boto3.client('s3')  # S3, EC2
s3_resource = boto3.resource('s3')

# Returns a list of all buckets owned by the authenticated sender of the request
bucket_list = s3_client.list_buckets()
# pp.pprint(bucket_list)

bucket_name = 'data-eng-resources'
# Returns the objects in a bucket
# bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='python')
bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='big-data/Adventure Works')
# pp.pprint(bucket_contents)

# Create instance of the bucket object
bucket = s3_resource.Bucket(bucket_name)
# print(bucket) # Returns s3.Bucket(name='data-eng-resources')

# Iterate through bucket and return obj and obj keys
# objects = bucket.objects.all()
# for obj in objects:
#    print(obj)
#    print(obj.key)

# Retrieves objects from Amazon S3
# File chatbot-intent.json - the body key contains the file which is contained in a StreamingBody object
# produces a binary string
# s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/chatbot-intent.json')
s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/happiness-2019.csv')
# pp.pprint(s3_object)

# strbody = s3_object['Body'].read()
# print(strbody)
# Use json.loads to load StreamingBody
# body = json.loads(strbody)
# print(body) # Returns a dictionary

# for csv files, use pandas dataframes
# pp.pprint(s3_object)

# not suitable for pandas as stored in string
# print(s3_object_new['Body'].read())

# for csv files, create a new dataframe | for text files use read method and handles as string
# df = pd.read_csv(s3_object['Body'])
# print(df)  # Prints dataframe

dict_to_upload = {'name': 'data', 'status': 1}

# Adds an object to a bucket. Must have Write permissions on a bucket to add an object to it.
# This method allows you to convert a python object into a serialized JSON object
s3_client.put_object(Body=json.dumps(dict_to_upload), Bucket=bucket_name, Key="Test249/y.json")

# Upload using file The upload_file method accepts a file name, a bucket name, and an object name. The method handles
# large files by splitting them into smaller chunks and uploading each chunk in parallel
s3_client.upload_file(Filename='new_json.json',
                      Bucket=bucket_name,
                      Key='Test249/y1.json')

# Uploading Dataframe requires string buffer A string buffer, also known as an in-memory string buffer or string
# stream, is used when working with DataFrames to efficiently convert the DataFrame's data into a string
# representation, such as CSV

# Create a pandas DataFrame
df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 1]])
# Initialize a String Buffer
str_buffer = io.StringIO()
# Convert DataFrame to CSV Format:
df.to_csv(str_buffer)
# Upload to Amazon S3
s3_client.put_object(Body=str_buffer.getvalue(),
                     Bucket=bucket_name,
                     Key='Test249/y.csv')
