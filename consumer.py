from kafka import KafkaConsumer
import json
import time


consumer = KafkaConsumer(
    'stock_analysis',
    bootstrap_servers=['localhost:9094'],
    auto_offset_reset='earliest', 
    enable_auto_commit=True, #constant updating
    group_id='stock-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Starting Kafka Consumer... Waiting for messages on topic 'stock_analysis'.")

for message in consumer:
    data = message.value

    print(f" Value(Deserialized): {data}")
consumer.close()
print("Kafka Consumer closed.")