from kafka import KafkaProducer
import json, time, random, os

KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "localhost:9092")
TOPIC = os.environ.get("KAFKA_TOPIC", "iot-data")

print(f"Connecting to Kafka at {KAFKA_BROKER}, topic: {TOPIC}")

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def generate_sensor_data():
    return {
        "device_id": f"sensor-{random.randint(1, 10)}",
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 50.0), 2),
        "timestamp": int(time.time())
    }

while True:
    data = generate_sensor_data()
    try:
        producer.send(TOPIC, data)
        print(f"Sent to Kafka: {data}")
    except Exception as e:
        print(f"Kafka error: {e}")
    time.sleep(2)
