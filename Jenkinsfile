pipeline {
    agent any

   environment {
    
        IMAGE_NAME = "mimouneayoub/skin-disease"
        IMAGE_TAG = "latest"
    }
    stages {
        stage('Checkout') {
            steps {
             git branch: 'main', url: 'https://github.com/mimouneayoub/skin-disease-detection.git'
            }
        } 
        stage('Creation of docker image') {
            steps {
                withDockerRegistry(credentialsId: 'docker-cred', url: 'https://index.docker.io/v1/') {
                    sh 'docker build -t mimouneayoub/skin-disease .'
                }
            }
        }
        stage('Push image to Docker Hub') {
            steps {
                withDockerRegistry(credentialsId: 'docker-cred', url: 'https://index.docker.io/v1/') {
                    sh 'docker push mimouneayoub/skin-disease'
                }
            }
        }
        stage('Creating docker container') {
            steps {
                withDockerRegistry(credentialsId: 'docker-cred', url: 'https://index.docker.io/v1/') {
                    sh 'docker run --name skin-disease-web -p 9000:9000 -d mimouneayoub/skin-disease' 
                }
            }
        }
        stage('Deploy to kubernates cluster'){
  			steps {
     			 sh 'kubectl apply -f deployment.yaml'
                 sh 'kubectl apply -f service.yaml'      
            }
        }
    }
}
