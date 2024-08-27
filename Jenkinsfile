pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t message-api:latest .'
            }
        }
        stage('Push to Registry') {
            steps {
                sh 'docker tag message-api:latest revathilakshmanan/message-api:latest'
                sh 'docker push revathilakshmanan/message-api:latest'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                  kubectl apply -f k8s/deployment.yaml
                  kubectl apply -f k8s/statefulset.yaml
                '''
            }
        }
    }
}
