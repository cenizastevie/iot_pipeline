@echo off

:: Check if required environment variables are set
if "%IAM_USER_ARN%"=="" (
    echo Error: IAM_USER_ARN environment variable is not set.
    exit /b 1
)

if "%K8S_USERNAME%"=="" (
    echo Error: K8S_USERNAME environment variable is not set.
    exit /b 1
)

:: Verify kubectl authentication
kubectl get nodes
if %errorlevel% neq 0 (
    echo Error: kubectl is not authenticated with the cluster. Please check your AWS credentials and kubeconfig.
    exit /b 1
)

:: Write the correct aws-auth.yaml structure
(
echo apiVersion: v1
echo kind: ConfigMap
echo metadata:
echo ^  name: aws-auth
echo ^  namespace: kube-system
echo data:
echo ^  mapUsers: ^|
echo ^    - userarn: %IAM_USER_ARN%
echo ^      username: %K8S_USERNAME%
echo ^      groups:
echo ^        - system:masters
) > aws-auth.yaml

:: Apply the updated ConfigMap
kubectl apply -f aws-auth.yaml --validate=false
if %errorlevel% neq 0 (
    echo Error: Failed to apply aws-auth ConfigMap.
    exit /b 1
)

echo aws-auth ConfigMap updated successfully.