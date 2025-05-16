import os
import logging
import random
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, from_unixtime
from pyspark.sql.types import StructType, StringType, DoubleType, LongType

# Define schema
schema = (
    StructType()
    .add("device_id", StringType())
    .add("temperature", DoubleType())
    .add("humidity", DoubleType())
    .add("timestamp", LongType())
    .add("city_code", StringType())
)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("SparkStreamingKafka")

logger.info("Starting Spark Streaming Kafka application.")

spark = SparkSession.builder \
    .appName("IoT Kafka Spark Stream") \
    .master("local[*]") \
    .getOrCreate()

# Get Kafka broker and topic from environment variables
kafka_broker = os.getenv("KAFKA_BROKER", "host.docker.internal:9092")  # Default to localhost:9092 if not set
kafka_topic = os.getenv("KAFKA_TOPIC", "iot-data")  # Default to "iot-data" if not set
bucket_name = os.getenv("BUCKET_NAME", "iot-temperature-bucket")  # Default to "iot-data-bucket" if not set

logger.info(f"Kafka broker: {kafka_broker}, Topic: {kafka_topic}, Bucket: {bucket_name}")

try:
    # Read stream from Kafka
    df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", kafka_broker) \
        .option("subscribe", kafka_topic) \
        .load()

    # Deserialize and process
    json_df = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")

    # Add date column for partitioning
    json_df = json_df.withColumn("date", from_unixtime(col("timestamp"), "yyyy-MM-dd"))

    # Simulate random errors
    if random.random() < 0.1:  # 10% chance of raising an error
        raise RuntimeError("Simulated random error in Spark Streaming application.")

    query = json_df.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    logger.info("Spark Streaming application is running.")
    query.awaitTermination()
except Exception as e:
    logger.error(f"An error occurred: {e}", exc_info=True)
    raise
