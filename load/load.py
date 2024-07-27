import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('weatherload')
local_file_path = '../dags/transformed_data/weather_data.csv'
s3_file_path='weather_data.csv'
bucket.upload_file(local_file_path, s3_file_path)