# Skin Disease Detection with VGG and SVM

![Skin Disease Detection]

## 📝 Project Overview

This MLOps project aims to develop a machine learning model for skin disease detection using advanced techniques. The project involves feature extraction using **VGG** (Visual Geometry Group) and prediction with **SVM** (Support Vector Machine). Additionally, a modern web application is built using **Flask** to provide a user-friendly interface for interacting with the model. Continuous integration and continuous deployment (CI/CD) are managed with **Jenkins**, automating the deployment of the web app into a **Kubernetes** cluster.

## 🧩 Key Components

1. **Model Development**
   - **Feature Extraction**: Utilizes the VGG network to extract features from images of skin lesions.
   - **Prediction**: Employs SVM to classify skin diseases based on the extracted features.

2. **Web Application**
   - **Flask**: A Python-based micro web framework used to develop the web application. The app provides an interface for users to upload skin images and receive predictions from the model.

3. **CI/CD Pipeline**
   - **Jenkins**: Automates the build, test, and deployment processes. The pipeline ensures that changes are continuously integrated and deployed to the Kubernetes cluster.
   - **Kubernetes**: Manages containerized application deployment, scaling, and operations.

## 📦 Project Setup

### Prerequisites

- Python 3.x
- Flask
- Docker
- Jenkins
- Kubernetes
- Minikube (for local Kubernetes cluster)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/skin-disease-detection.git
   cd skin-disease-detection
