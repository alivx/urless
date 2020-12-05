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
               sh "ls"
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
              sh 'bash build.sh run'
            },
            "secondTask" : {
               sh 'bash build.sh test'
            }
          )
      }
    }
  }
}