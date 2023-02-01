import boto3
import os

def upload_file_s3(filename, bucket, object_name):
    client = boto3.client("s3")
    client.upload_file(filename, bucket, object_name)

upload_file_s3(os.path.abspath("data/microdados_enem_2020/DADOS/MICRODADOS_ENEM_2020.csv"), "datalake-pedrosa-524095156763", "raw/enem/enem_csv/dataload=20230131/microdados_enem_2020.csv")