from kafka import KafkaProducer, KafkaConsumer
import json
from datetime import datetime, timedelta
from collections import defaultdict

consumer = KafkaConsumer(
    'orders-topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    group_id="stream-group"
)
