import boto3
from loguru import logger
import os
import sys
import subprocess


if __name__ == "__main__":
    creds = subprocess.run(["aws", "configure", "export-credentials", "--profile", "dbt-user", "--format", "env"])
    print(creds)
    