pipeline {
  agent any
  stages {
    stage('Fluffy Build') {
      steps {
        sh 'build.sh setup'
      }
    }
    stage('Fluffy Test') {
      parallel {
        stage('Backend') {
          steps {
            sh 'build.sh test'
          }
        }
        stage('Frontend') {
          steps {
            sh 'build.sh test'
          }
        }
        stage('Performance') {
          steps {
            sh 'build.sh test'
          }
        }
        stage('Static') {
          steps {
            sh 'build.sh test'
          }
        }
      }
    }
    stage('Fluffy Deploy') {
      steps {
        sh 'echo "ali 07eee196-fa9d-41b3-8b35-5ca7cfe87a2a"'
      }
    }
  }
}