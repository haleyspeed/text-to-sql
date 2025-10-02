import pandas as pd 
import boto3
import os

def clean_columns (tmp):
    """Removes whitespace, converts to lowercase, and replaces commas and other special characters with '_'"""
    tmp.columns = [c.lower().replace(' ', '_').replace(',', '_').replace('(', '_').replace(')', '').strip() for c in tmp.columns]
    return tmp


if __name__ == '__main__':
    local_folder = 'tmp/'
    if not os.path.exists(local_folder):
        os.mkdir(local_folder)

    bucket_name = 's3-haleygeek-dbt-data'
    bucket_path = 'painterdb/'
    download_bucket_filename = 'paint_database_v1.csv'
    download_bucket_key = bucket_path + download_bucket_filename
    download_local_filename = download_bucket_filename
    download_local_path = local_folder + download_local_filename
    
    client = boto3.client('s3')

    try:    
        client.download_file(
            bucket_name,
            download_bucket_key,
            download_local_path
        )
    except Exception as e: 
        print(e)    

    upload_bucket_filename = download_bucket_filename.replace('csv', 'parquet')
    upload_bucket_key = bucket_path + upload_bucket_filename
    upload_local_filename = upload_bucket_filename
    upload_local_path = local_folder + upload_local_filename

    upload_file = pd.read_csv(download_local_path)
    upload_file = clean_columns(upload_file)
    upload_file.to_parquet(upload_local_path, index = False)

    try:
        client.upload_file(
            upload_local_path,
            bucket_name,
            upload_bucket_key
        )
    except Exception as e:
        print(e)
