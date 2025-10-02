import pandas as pd 
import boto3
import os

# Reads the CSV from the S3 bucket and converts it to parquet

if __name__ == '__main__':
    local_folder = 'tmp'
    if not os.path.exists(local_folder):
        os.mkdir(local_folder)

    bucket_name = 's3-haleygeek-dbt-data'
    bucket_path = 'painterdb/'
    bucket_filename = 'paint_database_v1.csv'
    bucket_key = bucket_path + bucket_filename
    local_filename = bucket_filename
    local_path = local_folder + local_filename
    
    client = boto3.client('s3')

    try:    
        client.download_file(
            bucket_name,
            bucket_key,
            local_filename
        )
    except Exception as e: 
        print(e)    
