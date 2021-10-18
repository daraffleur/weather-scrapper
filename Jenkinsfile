pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
                sh 'python weather.py'
                
            }
        }

        stage('Git clone') {
            steps {
                
                sh 'rm -rf my_weather_scraper'
                sh 'https://github.com/KunalNK/my_weather_scraper.git'
                sh 'python app.py'                            
            }
        }
    }
}