
# Kafka setup

from kafka import KafkaProducer
import json

# Topic is like a database table
topic = "stock_analysis"


def init_producer():
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9094"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        retries=3,
        acks='all',
        request_timeout_ms=10000
    )
    return producer