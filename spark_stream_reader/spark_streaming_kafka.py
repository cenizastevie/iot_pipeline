from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

# Define schema
schema = StructType().add("sensor_id", StringType()).add("temperature", StringType())

spark = SparkSession.builder \
    .appName("IoT Kafka Spark Stream") \
    .master("local[*]") \
    .getOrCreate()

# Read stream from Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "host.docker.internal:9092") \
    .option("subscribe", "iot-data") \
    .load()

# Deserialize and process
json_df = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")

query = json_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
