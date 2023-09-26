import boto3
import pprint as pp
import json
import pandas as pd
import io

# Initialize S3 clients
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')


def read_csv_from_s3(bucket_name, object_key):
    """Read a csv file from S3 and return it as a DataFrame."""
    try:
        s3_object = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        df = pd.read_csv(s3_object['Body'])
        return df
    except Exception as e:
        print(f"Error reading csv from S3: {str(e)}")
        return None


def transform_csv_data(df):
    """Transform the DataFrame by averaging by species of fish."""
    try:
        df_transformation = df.groupby('Species').mean().reset_index()
        return df_transformation
    except Exception as e:
        print(f"Error transforming csv data: {str(e)}")
        return None


def upload_csv_to_s3(df, bucket_name, s3_destination_key):
    """Upload a DataFrame as a csv to Amazon S3."""
    try:
        str_buffer = io.StringIO()
        df.to_csv(str_buffer, index=False)
        s3_client.put_object(Body=str_buffer.getvalue(), Bucket=bucket_name, Key=s3_destination_key)
    except Exception as e:
        print(f"Error uploading csv to S3: {str(e)}")


if __name__ == "__main__":
    # State the bucket name and list of csv files
    bucket_name = 'data-eng-resources'
    csv_files = ['fish-market-mon.csv', 'fish-market-tues.csv', 'fish-market.csv']

    # Initialize an empty DataFrame to store the fish data of all csv files
    df = pd.DataFrame()

    # Iterate through each csv file and process
    for csv_file in csv_files:
        # Create the object key for the current csv file
        object_key = f'python/{csv_file}'

        # Read the fish market csv data from S3 using function
        df_new = read_csv_from_s3(bucket_name, object_key)
        # Call to the remaining functions
        df_transformation = transform_csv_data(df_new)
        df = pd.concat([df, df_transformation])

    print("\nTransformed DataFrame:")
    print(df)

    # Specify the destination key for the final uploaded csv
    s3_destination_key = 'Data249/fish/yuvraj.csv'

    # Upload the DataFrame as a csv to S3
    upload_csv_to_s3(df, bucket_name, s3_destination_key)
