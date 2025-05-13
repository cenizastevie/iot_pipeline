import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

# Define schema
schema = StructType().add("sensor_id", StringType()).add("temperature", StringType())

spark = SparkSession.builder \
    .appName("IoT Kafka Spark Stream") \
    .master("local[*]") \
    .getOrCreate()

# Get Kafka broker and topic from environment variables
kafka_broker = os.getenv("KAFKA_BROKER", "localhost:9092")  # Default to localhost:9092 if not set
kafka_topic = os.getenv("KAFKA_TOPIC", "iot-data")  # Default to "iot-data" if not set

# Read stream from Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", kafka_broker) \
    .option("subscribe", kafka_topic) \
    .load()

# Deserialize and process
json_df = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")

query = json_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
