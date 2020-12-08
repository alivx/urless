pipeline {
   agent { label 'appBuilder' }
   stages {
    stage('Clone Service') {
                steps {
                    git branch: 'master', url: 'https://github.com/alivx/urless.git'
                    sh label: 'Get current commit', script: 'git log --name-status HEAD^..HEAD  > current_commit.meta'
                    sh label: 'Save Build Meta Data', script: 'echo "${JOBNAME} -  ${BUILD_ID}" > build.meta'
                }
            }
        stage("Unit test"){
            agent {
                // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
                dockerfile {
                    filename 'Dockerfile'
                    dir 'build'
                    label 'my-defined-label'
                    args '-v /tmp:/tmp'
                }
            }
            steps{
                sh 'cd api;nosetests --with-xunit'
            }
        }
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
                      sleep 10
                      sh 'ssh root@09bff02a681c.mylabserver.com "docker stop urless "'
                   }
               }
           }
       }
   }
   post {
        always {
            junit 'api/*.xml'
        }
    }
}