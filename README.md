# Dockerized Flask Application Deployed on GKE

![GitHub repo size](https://img.shields.io/github/repo-size/neamulkabiremon/gcp-devops-project)
![GitHub last commit](https://img.shields.io/github/last-commit/neamulkabiremon/gcp-devops-project)
![GitHub license](https://img.shields.io/github/license/neamulkabiremon/gcp-devops-project)

## Project Overview
This is a **Flask application** containerized using **Docker** and deployed on **Google Kubernetes Engine (GKE)** with a fully automated **CI/CD pipeline** using **Cloud Build**.

### Tech Stack
- **Programming Language:** Python (Flask)
- **Containerization:** Docker
- **Orchestration:** Kubernetes (GKE)
- **CI/CD:** Google Cloud Build
- **Cloud Provider:** Google Cloud Platform (GCP)

## Features
- **Microservices-based architecture** using Docker
- **Automated deployments** with Cloud Build
- **Scalability & high availability** with Kubernetes
- **Production-ready configuration** with separate `development` and `production` environments

## Project Structure
```
gcp-devops-project/
│── Dockerfile                # Docker configuration file
│── cloudbuild.yaml           # Cloud Build CI/CD pipeline
│── gke.yaml                  # Kubernetes deployment YAML
│── app.py                    # Flask application
│── requirements.txt           # Python dependencies
│── README.md                 # Project documentation
```

## How to Run the Project Locally

### Clone the Repository
```bash
git clone https://github.com/neamulkabiremon/gcp-devops-project.git
cd gcp-devops-project
```

### Build and Run the Docker Container
```bash
docker build -t flask-app .
docker run -p 8080:8080 flask-app
```

### Access the App
Open your browser and go to:
```
http://localhost:8080
```

## Deploying on GKE

### Push Docker Image to GCP Artifact Registry
```bash
gcloud builds submit --config=cloudbuild.yaml
```

### Deploy to GKE
```bash
kubectl apply -f gke.yaml
```

### Check Deployment Status
```bash
kubectl get pods -n gcp-devops-prod
kubectl get services -n gcp-devops-prod
```

## CI/CD Pipeline (Cloud Build)
This project follows a **GitOps approach** where:
- A **push to `development`** triggers a deployment to `staging`.
- A **pull request to `main`** triggers a deployment to `production`.

### Automated pipeline includes:
✅ **Docker image build & push**  
✅ **Dynamic image substitution**  
✅ **Kubernetes deployment on GKE**  
✅ **Service exposure with LoadBalancer**  

## Live Deployment
- **Production URL:** [http://your-production-url](#)
- **Staging URL:** [http://your-staging-url](#)

## About the Author
📌 **Neamul Kabir Emon** | DevOps Engineer | Cloud & Security Enthusiast  
🔗 **LinkedIn:** (https://www.linkedin.com/in/neamul-kabir-emon)  
🔗 **GitHub:** (https://github.com/neamulkabiremon)  

## License
This project is licensed under the **MIT License** – feel free to use and modify it.

---

### 🔹 If you found this project helpful, don't forget to ⭐ it on GitHub!  
🔗 [GitHub Repository](https://github.com/neamulkabiremon/gcp-devops-project)

🚀 **Happy coding!** 🎯🔥
