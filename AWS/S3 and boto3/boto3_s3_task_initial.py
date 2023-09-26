import boto3
import pprint as pp
import json
import pandas as pd
import io

# Initialise the S3 client
s3_client = boto3.client('s3')
# s3_resource = boto3.resource('s3')

# bucket_list = s3_client.list_buckets()
# pp.pprint(bucket_list)

bucket_name = 'data-eng-resources'
# object_key = 'python/fish-market.csv'

# List of csv files on s3
csv_files = ['fish-market-mon.csv', 'fish-market-tues.csv', 'fish-market.csv']

# Identify Fish Market csv data on S3
# s3_object = s3_client.get_object(Bucket=bucket_name, Key=object_key)
# pp.pprint(s3_object)

# Initialise an empty DataFrame to store the fish data of all csv files
df = pd.DataFrame()

# Iterate through each csv file
for csv_file in csv_files:
    # Create the object key for the current csv file
    object_key = f'python/{csv_file}'

    # Read the fish market csv data from S3
    # S3_object is an instance of S3 client that retrieves objects from S3
    s3_object = s3_client.get_object(Bucket=bucket_name, Key=object_key)

    # For csv files, create a pandas DataFrame
    df_new = pd.read_csv(s3_object['Body'])

    # Transform the Data by averaging by species of fish
    # Using groupby species, mean, and reset index so the species column is not the default index
    df_transformation = df_new.groupby('Species').mean().reset_index()

    # Concatenate the DataFrames
    df = pd.concat([df, df_transformation])

# Calculate the overall average for each species for each table
df = df.groupby('Species').mean().reset_index()

print("\nTransformed DataFrame:")
print(df)

# Initialise a string buffer
str_buffer = io.StringIO()
# Convert DataFrame to csv format using string buffer and index false to remove integer column
df.to_csv(str_buffer, index=False)
# Upload to Amazon S3
s3_destination_key = 'Data249/fish/yuvraj.csv'

s3_client.put_object(Body=str_buffer.getvalue(),
                     Bucket=bucket_name,
                     Key=s3_destination_key)
