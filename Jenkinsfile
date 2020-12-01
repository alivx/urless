pipeline {
  agent any
  stages {
    stage('Fluffy Build') {
      steps {
        sh 'bash  build.sh setup'
      }
    }
    stage('Fluffy Test') {
        stage('Backend') {
          steps {
            sh 'bash  build.sh test'
          }
        }
    }
    stage('Fluffy Deploy') {
      steps{
            sh 'bash  build.sh zip'
      }
      steps {
        archiveArtifacts artifacts: 'ali.zip', fingerprint: true, followSymlinks: false, onlyIfSuccessful: true
      }
    }
  }
}