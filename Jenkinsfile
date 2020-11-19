pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'cd api;pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'cd api;python test.py'
      }
    }
  }
}