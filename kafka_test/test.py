from kafka import KafkaProducer, Kafkaconsumer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('test-topic', b'Hello, Kafka!')
producer.flush()