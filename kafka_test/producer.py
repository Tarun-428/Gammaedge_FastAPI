from kafka import KafkaProducer, KafkaConsumer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for i in range(5):
    message = {'number': i, 'timestamp': time.time()}
    producer.send('test-topic',key=b'user-1', value=message)
    print(f'Sent: {message}')
    time.sleep(1)
producer.send(
    "orders-topic",
    key=b"user-1",
    value={"order_id": 123, "amount": 49.99}
)
producer.flush()


