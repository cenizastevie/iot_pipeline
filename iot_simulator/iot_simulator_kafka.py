from kafka import KafkaProducer
import json, time, random, os
import logging

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

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("IoTSimulatorKafka")

logger.info("Starting IoT Simulator Kafka application.")

try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    logger.info(f"Kafka broker: {KAFKA_BROKER}, Topic: {TOPIC}")
except Exception as e:
    logger.error(f"Failed to connect to Kafka broker at {KAFKA_BROKER}: {e}", exc_info=True)
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
        # Simulate random errors
        if random.random() < 0.1:  # 10% chance of raising an error
            raise RuntimeError("Simulated random error in IoT Simulator.")

        producer.send(TOPIC, data)
        logger.info(f"Sent to Kafka: {data}")
    except Exception as e:
        logger.error(f"Kafka error: {e}", exc_info=True)
    time.sleep(2)
