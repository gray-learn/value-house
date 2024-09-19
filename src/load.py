import boto3
import pandas as pd
from io import StringIO

def load_to_s3(transform_data, bucket_name, file_name):
  # Initialize S3 client
  s3 = boto3.client('s3')

  # Save DataFrame to a CSV buffer
  csv_buffer = StringIO()
  transform_data.to_csv(csv_buffer, index=False)
  
  # Upload the CSV file to Amazon S3
  
  s3.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())
  
  print("Data uploaded to Amazon S3 successfully!")
