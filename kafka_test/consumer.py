from kafka import KafkaConsumer
import json

def safe_deserialize(data):
    if data is None:
        return None
    try:
        return json.loads(data.decode('utf-8'))
    except json.JSONDecodeError:
        print(f"Skipping malformed message: {data}")
        return None

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    group_id='batch-group',
    value_deserializer=safe_deserialize,
    max_poll_records=10,
)
while True:
    records = consumer.poll(timeout_ms=5000)
    for tp,consumer in records.items():
        for message in consumer:
            print(f'Received: {message.value},{message.key}')