import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
  print(event)
  
  for record in event['Records']:
    print(record['s3']['bucket']['name'])

  # for record in event['Records']:
  #     bucket = record['s3']['bucket']['name']
  #     key = unquote_plus(record['s3']['object']['key'])
  #     tmpkey = key.replace('/', '')
  #     download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
  #     upload_path = '/tmp/resized-{}'.format(tmpkey)
  #     s3_client.download_file(bucket, key, download_path)
  #     resize_image(download_path, upload_path)
  #     s3_client.upload_file(upload_path, '{}-resized'.format(bucket), key)
            