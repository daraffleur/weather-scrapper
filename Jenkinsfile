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
                
                sh 'sudo rm -rf my_yelp_reviews'
                sh 'git clone https://github.com/KunalNK/my_yelp_reviews.git'
                sh 'cd my_yelp_reviews'
                sh 'cat yelp_reviews_new.csv'
                
            }
        }
    }
}