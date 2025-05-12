# AWS ECR Docker Image Build and Push Instructions

## Prerequisites
1. Ensure you have AWS CLI installed and configured with the appropriate profile and permissions.
2. Ensure Docker is installed and running on your system.

---

## Steps to Build and Push `iot-simulator-repo` Image

1. Authenticate Docker to AWS ECR:
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 211626350366.dkr.ecr.us-east-1.amazonaws.com
   ```

2. Build the Docker image:
   ```bash
   docker build -t iot-simulator-repo .
   ```

3. Tag the Docker image:
   ```bash
   docker tag iot-simulator-repo:latest 211626350366.dkr.ecr.us-east-1.amazonaws.com/iot-simulator-repo:latest
   ```

4. Push the Docker image to AWS ECR:
   ```bash
   docker push 211626350366.dkr.ecr.us-east-1.amazonaws.com/iot-simulator-repo:latest
   ```

---

## Steps to Build and Push `spark-streamer-repo` Image

1. Authenticate Docker to AWS ECR:
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 211626350366.dkr.ecr.us-east-1.amazonaws.com
   ```

2. Build the Docker image:
   ```bash
   docker build -t spark-streamer-repo .
   ```

3. Tag the Docker image:
   ```bash
   docker tag spark-streamer-repo:latest 211626350366.dkr.ecr.us-east-1.amazonaws.com/spark-streamer-repo:latest
   ```

4. Push the Docker image to AWS ECR:
   ```bash
   docker push 211626350366.dkr.ecr.us-east-1.amazonaws.com/spark-streamer-repo:latest
   ```