# Weekly Schedule for Building the IoT Pipeline using CloudFormation

---

## Week 1: VPC and Networking
**Goal:** Set up the foundational networking layer.

**Tasks:**
- Create a VPC with public and private subnets using CloudFormation.
- Set up route tables, an Internet Gateway (IGW), and a NAT Gateway.
- Output subnet IDs for use in other CloudFormation templates.

**Deliverables:**
- A functional VPC with networking components ready for EKS deployment.

---

## Week 2: Kubernetes (EKS) Cluster
**Goal:** Deploy the Kubernetes cluster to orchestrate workloads.

**Tasks:**
- Create an Amazon EKS cluster using CloudFormation.
- Define node groups (EC2 instances) for running workloads.
- Set up IAM roles for EKS cluster management and worker nodes.

**Deliverables:**
- A fully functional EKS cluster ready to deploy applications.
- **File:** `cloudformation/eks.yaml`

---

## Week 3: ECR and IAM Roles
**Goal:** Set up container image storage and permissions.

**Tasks:**
- Define an ECR repository to store Docker images using CloudFormation.
- Create IAM roles and policies for:
  - EKS worker nodes to pull images from ECR.
  - CI/CD pipelines to push images to ECR.

**Deliverables:**
- ECR repository and IAM roles configured for image storage and access.

---

## Week 4: Application Load Balancer (ALB)
**Goal:** Manage external traffic for services.

**Tasks:**
- Create an Application Load Balancer (ALB) using CloudFormation.
- Define listener rules to route traffic to Kubernetes services (e.g., Grafana, APIs).

**Deliverables:**
- ALB configured to route traffic to Kubernetes services.

---

## Week 5: Monitoring, Logging, and Auto Scaling
**Goal:** Set up monitoring, logging, and scaling.

**Tasks:**
- Enable CloudWatch logging for:
  - EKS cluster and applications.
  - ALB network traffic.
- Set up metrics and alarms for resource utilization.
- Enable auto-scaling for:
  - EKS node groups based on workload.
  - ALB target groups to manage traffic spikes.

**Deliverables:**
- Monitoring and scaling mechanisms in place for the pipeline.

**Additional Task:**
- Deploy Amazon OpenSearch Service (formerly Elasticsearch Service) using CloudFormation:
  - Create an OpenSearch domain.
  - Configure access policies to allow the Spark application to write data.
  - Enable VPC access for secure communication.
  - Set up CloudWatch monitoring for the OpenSearch domain.

**Deliverables:**
- OpenSearch domain ready to ingest and index data.

---

## Week 6: CI/CD Pipeline
**Goal:** Automate the deployment process.

**Tasks:**
- Set up a CodePipeline with the following stages:
  - **Source Stage:** Pull code from GitHub or CodeCommit.
  - **Build Stage:** Use CodeBuild to:
    - Build Docker images for applications.
    - Push images to ECR.
  - **Deploy Stage:** Deploy Kubernetes manifests to the EKS cluster using CodeDeploy or a custom script.
- Create a `buildspec.yml` file for CodeBuild to define build steps.
- Ensure IAM roles and permissions are in place for CodePipeline and CodeBuild.

**Deliverables:**
- A fully functional CI/CD pipeline automating the build and deployment process.

---

## Week 7: IoT Simulator Deployment
**Goal:** Deploy the IoT Simulator to generate mock sensor data.

**Tasks:**
- Write a Kubernetes manifest (`simulator-deployment.yaml`) for the IoT Simulator.
- Define resource requests and limits for the IoT Simulator pods.
- Deploy the IoT Simulator to the EKS cluster.

**Deliverables:**
- IoT Simulator running on EKS, generating mock sensor data.

---

## Week 8: Spark Pods Deployment
**Goal:** Deploy Spark jobs for real-time data processing.

**Tasks:**
- Write Kubernetes manifests (`spark-deployment.yaml`) for Spark driver and executor pods.
- Define resource requests and limits for Spark pods.
- Deploy Spark jobs to the EKS cluster.
- Test the pipeline end-to-end (IoT Simulator → Kafka → Spark → DynamoDB).

**Deliverables:**
- Spark pods running on EKS, processing real-time data streams.

---

## Final Deliverables
By the end of this schedule, you will have:
- A fully functional IoT pipeline deployed on AWS using CloudFormation.
- CI/CD pipeline automating the build and deployment process.
- IoT Simulator and Spark pods running on EKS, processing real-time data.