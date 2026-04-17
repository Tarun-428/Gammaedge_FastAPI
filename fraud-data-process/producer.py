from kafka import KafkaProducer, KafkaConsumer
import json
import time
import random
from datetime import datetime

producer=KafkaProducer(bootstrap_servers='localhost:9092',
                       value_serializer=lambda v:json.dumps(v).encode('utf-8'),
                        key_serializer=lambda k: str(k).encode('utf-8'))

users = [
    {"user_id": 1, "name": "Tarun", "email": "tarun@gmail.com", "city": "Indore"},
    {"user_id": 2, "name": "Amit", "email": "amit@gmail.com", "city": "Delhi"},
    {"user_id": 3, "name": "Neha", "email": "neha@gmail.com", "city": "Mumbai"}
]
order_id = 100
while True:
    user = random.choice(users)
    if random.random() < 0.3:
        user['city'] = random.choice(["Indore","Delhi","Mumbai","Bangalore"])
    user_event = {
        "user_id": user['user_id'],
        "name": user['name'],
        "email": user['email'],
        "city": user['city'],
        "updated_at": str(datetime.now())
    }

    producer.send(
        "users-topic",
        key=user["user_id"],
        value=user_event
    )
    print(f"Sent user event: {user_event}")

    order_id += 1
    order_event={
        "order_id": order_id,
        "user_id": user['user_id'],
        "amount": random.randint(100,20000),
        "status": "PLACED",
        "created_at": str(datetime.now())
    }
    producer.send(
        "orders-topic",
        key=user["user_id"],
        value=order_event
    )
    print(f"Sent order event: {order_event}")   
    time.sleep(2)
