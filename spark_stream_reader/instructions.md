# Instructions for Running Spark Stream Reader

1. Ensure Docker is installed and running on your system.
2. Open a terminal and navigate to the project directory:
   ```
   cd spark_stream_reader
   ```
3. Build the Docker image:
   ```
   docker build -t spark-streamer .
   ```
4. Run the Docker container:
   ```
   docker run --add-host=host.docker.internal:host-gateway spark-streamer
   ```
5. After running, stop and remove the container if necessary:
   ```
   docker ps
   docker stop <container_id>
   docker rm <container_id>
   ```