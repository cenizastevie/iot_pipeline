# Build the Docker image
docker build -t iot-simulator .

# Run the Docker container with environment variables and host configuration
docker run --add-host=host.docker.internal:host-gateway `
  -e KAFKA_BROKER=host.docker.internal:9092 `
  -e KAFKA_TOPIC=iot-data `
  iot-simulator

docker run  -it --rm --add-host=host.docker.internal:host-gateway -e KAFKA_BROKER=host.docker.internal:9092 -e KAFKA_TOPIC=iot-data iot-simulator

# Access the Kafka container and consume messages from the topic
docker exec -it <kafka-container-id> bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic iot-data --from-beginning