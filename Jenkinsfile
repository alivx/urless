pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'hostname'
      }
    }
    stage('test') {
      steps {
        sh 'cd api;python test.py'
      }
    }
  }
}