# Kubernetes Instructions for IoT Pipeline

## Deployments

Apply the deployments for the IoT simulator and Spark streamer:
```
kubectl apply -f iot-simulator-deployment.yaml
kubectl apply -f spark-streamer-deployment.yaml
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