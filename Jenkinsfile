pipeline {
  agent any
  stages {
    stage('Fluffy Build') {
      steps {
        sh 'bash  build.sh setup'
      }
    }
    stage('Fluffy Test') {
      parallel {
        stage('Backend') {
          steps {
            sh 'bash  build.sh test'
          }
        }
        stage('Frontend') {
          steps {
            sh 'bash  build.sh test'
          }
        }
        stage('Performance') {
          steps {
            sh 'bash  build.sh test'
          }
        }
        stage('Static') {
          steps {
            sh 'bash  build.sh test'
          }
        }
      }
    }
    stage('Fluffy Deploy') {
      steps {
        archive '*'
        archiveArtifacts artifacts: '**/*.*', fingerprint: true, followSymlinks: false, onlyIfSuccessful: true
      }
    }
  }
}