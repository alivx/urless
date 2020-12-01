pipeline {
  agent any
  stages {
    stage('URLess Build') {
      steps {
        sh 'bash build.sh setup'
      }
    }
    stage('URLess Test') {
      steps {
        sh 'bash build.sh test'
      }
    }
    stage('URLess Deploy') {
      steps{
        sh 'bash build.sh zip'
      }
    }
    stage('URLess Archive') {
      steps {
        archiveArtifacts artifacts: 'ali.zip', fingerprint: true, followSymlinks: false, onlyIfSuccessful: true
      }
    }
  }
}