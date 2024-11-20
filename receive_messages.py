import boto3

sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/474668387337/data-ingestion-queue'

response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1
)

for message in response.get('Messages', []):
    print("Recibido:", message['Body'])
    # Eliminar mensaje después de procesarlo
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message['ReceiptHandle']
    )
