pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
                sh 'python weather.py'
                
            }
        }

        stage('Test-1') {
            steps {
                sh 'python --version'
                sh 'python weather.py'
                
            }
        }
    }
}