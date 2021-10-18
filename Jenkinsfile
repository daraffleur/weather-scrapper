pipeline {
    agent any
    stages {
        stage('git repo & clean') {
            steps {
               
                sh "git clone https://github.com/KunalNK/my_weather_scraper.git"
               
            }
        }
        stage('install') {
            steps {
                sh "python3 weather.py"
            }
        }
    }
}