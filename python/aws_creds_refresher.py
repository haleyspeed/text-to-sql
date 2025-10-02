import boto3
from loguru import logger
import os
import sys
import subprocess


if __name__ == "__main__":
    #sso_session_name = 'dbt_user'
    #sso_start_url = "https://haleygeek.awsapps.com/start/#"
    #sso_region = 'us-west-2'
    #subprocess.run(["aws", "configure", "sso", sso_session_name, sso_start_url, sso_region,'',sso_region,'text','dbt-user'])
    
    creds = subprocess.run(["aws", "configure", "export-credentials", "--profile", "dbt-user", "--format", "env"])
    print(creds)
    