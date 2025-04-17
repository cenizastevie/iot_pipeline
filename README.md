# IoT Real-Time Data Pipeline

## Description
This repository demonstrates a scalable IoT data processing system using Python, Kafka, Spark Streaming, Kubernetes, and AWS. It leverages AWS services like EKS, DynamoDB, and CloudFormation for automation, fault tolerance, and real-time analytics. Features include IoT data simulation, dashboards with Grafana, and end-to-end testing capabilities.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Running the Project](#running-the-project)
   - [Running the CloudFormation Stacks](#running-the-cloudformation-stacks)
5. [Use Case](#use-case)
6. [Technology Stack](#technology-stack)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview
This IoT data pipeline is designed for real-time ingestion, processing, and storage of sensor data. It employs Kafka for message streaming, Spark Streaming for real-time processing, and DynamoDB for scalable storage. The Kubernetes cluster hosted on AWS ensures scalability and fault tolerance, while Grafana provides actionable insights through interactive dashboards.

---

## Features
- **IoT Data Simulator:** Generates mock sensor data using Python and sends it to Kafka topics.
- **Kafka Integration:** Real-time data ingestion with Kafka.
- **Spark Streaming:** Processes data streams to detect anomalies and trends.
- **NoSQL Database:** Scalable storage solution with DynamoDB or MongoDB.
- **Kubernetes Orchestration:** Manages containerized applications for Spark and Kafka.
- **AWS CloudFormation Template:** Automates infrastructure setup on AWS.
- **Monitoring and Visualization:** Grafana dashboards and alerts for real-time analytics.

---

## Architecture
![Architecture Diagram Placeholder](#)  
**Key Components:**
1. IoT Data Simulator (Python)
2. Kafka Topics for message streaming
3. PySpark applications on Kubernetes for data processing
4. DynamoDB for NoSQL storage
5. AWS-managed resources (EKS, MSK, DynamoDB)

---

## Getting Started

### Prerequisites
- Python 3.x
- Docker
- Kubernetes CLI (`kubectl`)
- AWS account with IAM roles configured
- Tools: Kafka, PySpark, Grafana

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iot-real-time-data-pipeline.git
   cd iot-real-time-data-pipeline
   ```

### Running the Project
1. Start the IoT Data Simulator:
   ```bash
   python simulator.py
   ```
2. Start Kafka and create necessary topics:
   ```bash
   ./bin/kafka-server-start.sh config/server.properties
   ./bin/kafka-topics.sh --create --topic sensor-data --bootstrap-server localhost:9092
   ```
3. Deploy the Spark Streaming application on Kubernetes:
   ```bash
   kubectl apply -f spark-job.yaml
   ```
4. Monitor the pipeline using Grafana dashboards.

---

### Running the CloudFormation Stacks

1. **Deploy the VPC Stack:**
   Run the following command to create the VPC and networking components:
   ```bash
   aws cloudformation create-stack --stack-name iot-vpc-stack --template-body file://cloudformation/vpc.yaml --capabilities CAPABILITY_NAMED_IAM --profile iot-profile
   ```

2. **Deploy the EKS Stack:**
   After the VPC stack is successfully created, run the following command to deploy the EKS cluster:
   ```bash
   aws cloudformation create-stack --stack-name iot-eks-stack --template-body file://cloudformation/eks.yaml --capabilities CAPABILITY_NAMED_IAM --profile iot-profile
   ```

3. **Deploy the ECR Stack:**
   Run the following command to create the ECR repository:
   ```bash
   aws cloudformation create-stack --stack-name iot-ecr-stack --template-body file://cloudformation/ecr.yaml --capabilities CAPABILITY_NAMED_IAM --profile iot-profile
   ```

4. **Verify the Stacks:**
   Use the following command to check the status of the stacks:
   ```bash
   aws cloudformation describe-stacks --stack-name <stack-name> --profile iot-profile
   ```

5. **Delete the Stacks:**
   To delete the CloudFormation stacks, use the following commands:
   - Delete the EKS stack:
     ```bash
     aws cloudformation delete-stack --stack-name iot-eks-stack --profile iot-profile
     ```
   - Delete the VPC stack:
     ```bash
     aws cloudformation delete-stack --stack-name iot-vpc-stack --profile iot-profile
     ```
   - Delete the ECR stack:
     ```bash
     aws cloudformation delete-stack --stack-name iot-ecr-stack --profile iot-profile
     ```
   Verify the deletion status using:
   ```bash
   aws cloudformation describe-stacks --stack-name <stack-name> --profile iot-profile
   ```

#### Required IAM Permissions
Ensure that the IAM user or role executing the CloudFormation stacks has the following permissions:
- `iam:CreateRole`
- `iam:DeleteRole`
- `iam:AttachRolePolicy`
- `iam:DetachRolePolicy`
- `iam:PassRole`
- `ec2:*` (for VPC and networking resources)
- `eks:*` (for EKS cluster creation)
- `tag:GetResources`
- `tag:TagResources`
- `tag:UntagResources`

#### Additional Required IAM Permissions
Ensure that the IAM user or role executing the ECR stack has the following permissions:
- `ecr:CreateRepository`
- `ecr:DeleteRepository`
- `ecr:PutLifecyclePolicy`
- `ecr:GetLifecyclePolicy`
- `ecr:ListTagsForResource`
- `ecr:TagResource`
- `ecr:UntagResource`

Refer to the [AWS Knowledge Center](https://repost.aws/knowledge-center/cloudformation-tagging-permission-error) for more details on resolving tagging permission errors.

---

## Use Case
This pipeline is tailored for horse racing analytics, leveraging sensor data to monitor:
- **Soil Conditions:** Track moisture, compaction, and temperature for optimal racing surfaces.
- **Weather Monitoring:** Real-time updates on temperature, humidity, and wind conditions.
- **Performance Insights:** Analyze horse performance metrics in relation to environmental factors.

This enables race organizers and trainers to make data-driven decisions for safety and performance optimization.

---

## Technology Stack
- **Programming Language:** Python
- **Streaming Platform:** Apache Kafka
- **Processing Framework:** Apache Spark Streaming
- **Database:** AWS DynamoDB or MongoDB
- **Container Orchestration:** Kubernetes (AWS EKS)
- **Visualization:** Grafana
- **Infrastructure Automation:** AWS CloudFormation

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

aws cloudformation create-stack --stack-name iot-vpc-stack --template-body file://vpc.yaml --capabilities CAPABILITY_NAMED_IAM --profile iot-profile