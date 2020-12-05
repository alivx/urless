pipeline {
  agent any
  stages {
    stage('URLess Build') {
      steps {
        sh 'bash build.sh build'
      }
    }
    stage('URLess Test') {
      steps {
        sh 'bash build.sh test'
      }
    }
    stage('Publish') {
      steps {
        parallel (
            "firstTask" : {
              sh 'bash build.sh push'
            },
            "secondTask" : {
               sh "scp build.sh root@09bff02a681c.mylabserver.com:/root/"
            }
          )
      }
    }
    stage('URLess Pull') {
      steps {
        sh 'bash build.sh pull'
      }
    }
    stage('Run and test') {
      steps {
        parallel (
            "firstTask" : {
              sh 'ssh root@09bff02a681c.mylabserver.com "docker run --rm -d --name urless -p 8000:8000 alivx/urless:latest"'
            },
            "secondTask" : {
               sh 'ssh root@09bff02a681c.mylabserver.com "docker run --rm  alivx/urless:$(getCommitIT) test"'
            }
          )
      }
    }
  }
}