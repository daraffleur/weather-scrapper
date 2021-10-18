pipeline {
    agent any
    stages {
        stage('git repo & clean') {
            steps {
                sh "rm -rf my_weather_scraper"
                sh "git clone https://github.com/KunalNK/my_weather_scraper.git"
               
            }
        }
        stage('install') {
            steps {
                sh "python weather.py"
            }
        }
    }
}