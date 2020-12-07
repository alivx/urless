pipeline {
   agent { label 'appBuilder' }
   stages {
       stage('Check Code') {
           parallel {
               stage('safety check') {
                   steps {
                       sh 'docker run --rm --volume $(pwd) pyupio/safety:latest safety check'
                   }
               }
               stage('bandit') {
                   steps {
                       sh 'docker run --rm --volume $(pwd) secfigo/bandit:latest'
                   }
               }
               stage('python-taint check') {
                   steps {
                       sh 'docker run --rm --volume $(pwd) vickyrajagopal/python-taint-docker pyt .'
                   }
               }
               stage('flake8 check') {
                   steps {
                       sh 'docker run -i --rm -v $(pwd):/apps alpine/flake8:3.5.0  .'
                   }
               }
           }
       }
       stage('Build') {
           steps {
              sh 'bash build.sh build'
           }
       }
       stage('Push') {
           steps {
              sh 'bash build.sh push'
           }
       }
       stage('Pull') {
           steps {
              sh 'bash build.sh pull'
           }
       }
       stage('Deploy') {
           parallel {
               stage('RUN') {
                   steps {
                      sh 'ssh root@09bff02a681c.mylabserver.com "docker stop urless; docker run --rm -d --name urless -p 8000:8000 alivx/urless:latest"'
                   }
               }
               stage('Stop') {
                   steps {
                      sh 'ssh root@09bff02a681c.mylabserver.com "docker stop urless "'
                   }
               }
           }
       }
   }
}