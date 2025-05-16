# Kubernetes Instructions for IoT Pipeline

## AWS EKS Configuration

To edit the AWS auth configmap:
```
kubectl edit -n kube-system configmap/aws-auth
```

To update your kubeconfig file for accessing your EKS cluster, run the following command:
```
aws eks update-kubeconfig --region us-east-1 --name IoT-EKS-Cluster --profile steven
```
Replace `us-east-1` with your AWS region (e.g., `us-west-2`) and `IoT-EKS-Cluster` with the name of your EKS cluster.

Set the following environment variables for AWS authentication:
```
set IAM_USER_ARN=arn:aws:iam::123456789012:user/YourUser
set K8S_USERNAME=your-username
update-aws-auth.bat
```

### Create Kafka Namespace

Create the Kafka namespace:
```
kubectl create namespace kafka
```

### Install Strimzi in the Kafka Namespace

Install Strimzi:
```
kubectl create -f https://strimzi.io/install/latest?namespace=kafka -n kafka
```

Monitor the Strimzi installation:
```
kubectl get pod -n kafka --watch
kubectl logs deployment/strimzi-cluster-operator -n kafka -f
```

Deploy a single-node Kafka cluster:
```
kubectl apply -f https://strimzi.io/examples/latest/kafka/kafka-single-node.yaml -n kafka
kubectl wait kafka/my-cluster --for=condition=Ready --timeout=300s -n kafka
```

This ensures that your local `kubectl` is configured to interact with the specified EKS cluster.

## Deployments

Apply the deployments for the IoT simulator, Spark streamer, and Kafka in their respective namespaces:
```
kubectl apply -f iot-simulator-deployment.yaml -n kafka
kubectl apply -f spark-streamer-deployment.yaml -n kafka
```

## Checking Pods

List all pods in a specific namespace:
```
kubectl get pods -n <namespace>
```

Watch pods in a specific namespace:
```
kubectl get pods -n <namespace> -w
```

## Viewing Logs

View logs for a specific pod:
```
kubectl logs <pod-name> -n <namespace>
```

View logs for a specific container in a pod:
```
kubectl logs <pod-name> -c <container-name> -n <namespace>
```

Follow logs for a specific pod:
```
kubectl logs -f <pod-name> -n <namespace>
```

## Filtering Pods by Label

Get pods with the label `app=iot-simulator`:
```
kubectl get pods -l app=iot-simulator -n iot
```

Get pods with the label `app=spark-streamer`:
```
kubectl get pods -l app=spark-streamer -n kafka
```

Restart the IoT simulator deployment:
```
kubectl rollout restart deployment iot-simulator -n kafka
```

## Deleting Deployments

Delete the IoT simulator deployment:
```
kubectl delete deployment iot-simulator -n kafka
```

Delete the Spark streamer deployment:
```
kubectl delete deployment spark-streamer -n kafka
```

Delete the Zookeeper deployment:
```
kubectl delete deployment zookeeper -n kafka
```