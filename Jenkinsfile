pipeline {
  agent any
  stages {
    stage('URLess Setup') {
      steps {
        sh 'bash build.sh setup'
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
                            sh 'bash build.sh zip'

                  },
                  "secondTask" : {
                      sh "ls"
                  }
              )
          }
    }
    stage('URLess Archive') {
      steps {
        archiveArtifacts artifacts: 'ali.zip', fingerprint: true, followSymlinks: false, onlyIfSuccessful: true
      }
    }
  }
}