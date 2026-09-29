# DevOps Demo

End-to-end DevOps portfolio project demonstrating containerization, CI/CD automation, Infrastructure as Code, Kubernetes deployment and monitoring on AWS.

## Architecture

```text
Developer
    |
    | git push
    v
GitHub
    |
    v
GitHub Actions CI
    |
    +--> Python tests
    +--> Trivy security scan
    +--> Docker build
    |
    v
GitHub Container Registry (GHCR)
    |
    | CI successful
    v
GitHub Actions CD
    |
    | OIDC authentication
    v
AWS IAM
    |
    v
Amazon EKS
    |
    v
Kubernetes Deployment
    |
    +--> Pods
    |
    v
Kubernetes Service
```

## Technologies

- Python / Flask
- Docker
- Docker Compose
- Kubernetes
- AWS EKS
- AWS IAM
- Terraform
- GitHub Actions
- GitHub Container Registry (GHCR)
- Trivy
- Prometheus

## Project Structure

```text
DevOps-demo/
├── app/
│   └── backend/
│       ├── app.py
│       ├── requirements.txt
│       └── Dockerfile
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform/
│   ├── main.tf
│   └── variables.tf
│
├── monitoring/
│   └── prometheus.yml
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── docker-compose.yml
└── README.md
```

## Local Development

Build and start the application:

```bash
docker compose up --build
```

Application:

```text
http://localhost:5000
```

Health check:

```text
http://localhost:5000/health
```

Tasks endpoint:

```text
http://localhost:5000/tasks
```

## CI Pipeline

GitHub Actions automatically runs the CI pipeline after changes are pushed to the repository.

The pipeline:

1. Checks out the source code.
2. Installs Python dependencies.
3. Runs automated tests.
4. Performs a security scan with Trivy.
5. Builds the Docker image.
6. Publishes the image to GitHub Container Registry.

Docker images are tagged using the Git commit SHA, allowing each deployment to be linked to a specific version of the source code.

## CD Pipeline

A separate CD workflow runs after the CI workflow completes successfully on the `main` branch.

The deployment pipeline:

1. Authenticates GitHub Actions to AWS using OpenID Connect (OIDC).
2. Assumes an AWS IAM role without storing long-lived AWS credentials in GitHub.
3. Configures `kubectl` for the Amazon EKS cluster.
4. Applies Kubernetes manifests.
5. Updates the Kubernetes Deployment with the Docker image produced by CI.
6. Waits for the Kubernetes rollout to complete.

## Kubernetes

Deploy manually with:

```bash
kubectl apply -f k8s/
```

Check resources:

```bash
kubectl get pods
kubectl get deployments
kubectl get services
```

Check deployment rollout:

```bash
kubectl rollout status deployment/devops-demo
```

The Kubernetes Deployment manages application Pods and provides self-healing and rolling updates.

The Kubernetes Service exposes the application to network traffic.

## AWS Authentication

GitHub Actions authenticates to AWS using OIDC.

```text
GitHub Actions
      |
      | OIDC token
      v
AWS IAM Role
      |
      v
Amazon EKS
```

This avoids storing long-lived AWS access keys in GitHub Actions secrets.

## Infrastructure as Code

Terraform is used to define and provision AWS infrastructure required by the project.

Typical workflow:

```bash
cd terraform

terraform init
terraform validate
terraform plan
terraform apply
```

Infrastructure can be removed with:

```bash
terraform destroy
```

> AWS resources may generate charges.

## Security

The project includes several security practices:

- Trivy vulnerability scanning
- GitHub OIDC authentication to AWS
- IAM role-based access
- No long-lived AWS credentials required by the deployment workflow
- Immutable Docker image identification using Git commit SHA

## Monitoring

Prometheus configuration is included in the `monitoring/` directory and demonstrates application monitoring and metrics collection.

## What This Project Demonstrates

This project demonstrates practical knowledge of:

- Linux and container workflows
- Docker image creation
- CI/CD pipeline design
- Kubernetes deployments and services
- AWS EKS
- AWS IAM and OIDC
- Infrastructure as Code with Terraform
- Container security scanning
- Monitoring with Prometheus
- Automated application deployment

## Author

Jakub Sikora

Junior DevOps portfolio project.
