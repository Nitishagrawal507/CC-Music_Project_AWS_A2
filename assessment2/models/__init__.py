import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
s3 = boto3.client('s3')
from . import aws_login, aws_music, aws_subs, aws_img
