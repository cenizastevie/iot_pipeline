from kafka import KafkaProducer
import json, time, random, os

KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "localhost:9092")
TOPIC = os.environ.get("KAFKA_TOPIC", "iot-data")

# Validate Kafka broker and topic
if not KAFKA_BROKER:
    raise ValueError("KAFKA_BROKER environment variable is not set.")
if not TOPIC:
    raise ValueError("KAFKA_TOPIC environment variable is not set.")

print(f"Connecting to Kafka at {KAFKA_BROKER}, topic: {TOPIC}")

CITIES = {
    "X7A9": "Tokyo",
    "B3KQ": "New York",
    "P8L2": "London",
    "Z4MN": "Sydney",
    "J9RT": "Paris",
    "C2VX": "Dubai",
    "L5YW": "Singapore",
    "T3KP": "Berlin",
    "M7QX": "Toronto",
    "R6ZN": "Cape Town"
}

try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
except Exception as e:
    raise RuntimeError(f"Failed to connect to Kafka broker at {KAFKA_BROKER}: {e}")

def generate_sensor_data():
    city_code = random.choice(list(CITIES.keys()))
    return {
        "device_id": f"sensor-{random.randint(1, 10)}",
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 50.0), 2),
        "timestamp": int(time.time()),
        "city_code": city_code,
    }

while True:
    data = generate_sensor_data()
    try:
        producer.send(TOPIC, data)
        print(f"Sent to Kafka: {data}")
    except Exception as e:
        print(f"Kafka error: {e}")
    time.sleep(2)
