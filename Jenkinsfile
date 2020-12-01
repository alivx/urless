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
      steps{
      parallel{
        zip:{
          sh 'bash build.sh zip'
        }
        list:{
          sh 'ls'
        }
      }
      }
    }
    stage('URLess Archive') {
      steps {
        archiveArtifacts artifacts: 'ali.zip', fingerprint: true, followSymlinks: false, onlyIfSuccessful: true
      }
    }
  }
}