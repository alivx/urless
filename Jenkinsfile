pipeline {
  agent appBuilder
  stages {
    stage('URLess Setup') {
      steps {
        sh 'bash build.sh build'
      }
    }
    stage('URLess Test') {
      steps {
        sh 'bash build.sh test'
      }
    }
    stage('URLess Zip') {
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
  }
}