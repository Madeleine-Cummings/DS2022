#!/usr/bin/python3

import boto3
import os
import requests

def download_file(url, filename):
    """Download a file from a given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad response
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded successfully: {filename}")

def upload_to_s3(bucket_name, file_name, object_name):
    """Upload a file to an S3 bucket."""
    s3_client = boto3.client('s3', region_name='us-east-1')
    s3_client.upload_file(file_name, bucket_name, object_name)
    print(f"File uploaded successfully: {object_name} to bucket {bucket_name}")

def generate_presigned_url(bucket_name, object_name, expires_in):
    """Generate a presigned URL for an S3 object."""
    s3_client = boto3.client('s3')
    response = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_name},
        ExpiresIn=expires_in
    )
    return response

if __name__ == "__main__":
    # URL of the GIF file
    gif_url = "https://c.tenor.com/P3lOJQM_ik4AAAAC/tenor.gif"
    output_file = "silly_animal.gif"
    
    # S3 parameters
    bucket_name = "ds2022-uwg9at"  # Replace with your S3 bucket name
    object_name = "home/madeleine/silly_animal.gif"
    expires_in = 604800  # 7 days

    # Fetch the GIF file
    download_file(gif_url, output_file)

    # Upload to S3
    upload_to_s3(bucket_name, output_file, object_name)

    # Generate and output the presigned URL
    presigned_url = generate_presigned_url(bucket_name, object_name, expires_in)
    print(f"Presigned URL (valid for 7 days): {presigned_url}")
