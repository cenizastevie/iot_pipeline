# Kubernetes Instructions for IoT Pipeline

## AWS EKS Configuration

To update your kubeconfig file for accessing your EKS cluster, run the following command:
```
aws eks update-kubeconfig --region <region-code> --name <my-cluster>
```

Replace `<region-code>` with your AWS region (e.g., `us-west-2`) and `<my-cluster>` with the name of your EKS cluster.

This command ensures that your local `kubectl` is configured to interact with the specified EKS cluster.


## Deployments

Apply the deployments for the IoT simulator and Spark streamer:
```
kubectl apply -f iot-simulator-deployment.yaml
kubectl apply -f spark-streamer-deployment.yaml
kubectl apply -f kafka-deployment.yaml
```

## Checking Pods

List all pods:
```
kubectl get pods
```

## Viewing Logs

View logs for a specific pod:
```
kubectl logs <pod-name>
```

View logs for a specific container in a pod:
```
kubectl logs <pod-name> -c <container-name>
```

Follow logs for a specific pod:
```
kubectl logs -f <pod-name>
```

## Filtering Pods by Label

Get pods with the label `app=iot-simulator`:
```
kubectl get pods -l app=iot-simulator
```

Get pods with the label `app=spark-streamer`:
```
kubectl get pods -l app=spark-streamer
```

## Deleting Deployments

Delete the IoT simulator deployment:
```
kubectl delete deployment iot-simulator
```

Delete the Spark streamer deployment:
```
kubectl delete deployment spark-streamer
```

Delete the Zookeeper deployment:
```
kubectl delete deployment zookeeper
```