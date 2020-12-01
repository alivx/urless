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
        stage('zipping') {
          steps {
            sh 'bash  build.sh zip'
          }
        }
      }
    }
    stage('Fluffy Deploy') {
      steps {
        archiveArtifacts artifacts: '**/*.*', excludes: '.git', fingerprint: true, followSymlinks: false, onlyIfSuccessful: true
      }
    }
  }
}