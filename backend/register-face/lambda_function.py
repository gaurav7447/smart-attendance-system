import json
import boto3
import base64
import uuid
from datetime import datetime

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')

BUCKET_NAME = 'smart-attendance-face-storage'
COLLECTION_ID = 'attendance-face-collection'

table = dynamodb.Table('registered-users')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        name = body['name']
        profession = body['profession']
        image_data = body['image']

        image_bytes = base64.b64decode(image_data)

        user_id = str(uuid.uuid4())

        image_key = f"registered-faces/{user_id}.jpg"

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=image_key,
            Body=image_bytes,
            ContentType='image/jpeg'
        )

        response = rekognition.index_faces(
            CollectionId=COLLECTION_ID,
            Image={
                'S3Object': {
                    'Bucket': BUCKET_NAME,
                    'Name': image_key
                }
            },
            ExternalImageId=user_id,
            DetectionAttributes=[]
        )

        face_records = response['FaceRecords']

        if len(face_records) == 0:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'No face detected'
                })
            }

        face_id = face_records[0]['Face']['FaceId']

        table.put_item(
            Item={
                'id': user_id,
                'name': name,
                'profession': profession,
                'imageKey': image_key,
                'faceId': face_id,
                'registeredAt': str(datetime.now())
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'User registered successfully',
                'userId': user_id
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }