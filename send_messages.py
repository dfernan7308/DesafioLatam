import boto3

sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/474668387337/data-ingestion-queue'

# Enviar un mensaje
message = {"sensor_id": 123, "value": 45.67}
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=str(message)
)

print("Mensaje enviado:", response['MessageId'])
