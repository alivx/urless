pipeline {
  agent { docker { image 'python:3.7.2'} }
  stages {
    stage('build') {
      steps {
        sh 'ifconfig'
        sh 'hostname'
        sh 'pip install -r api/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'ifconfig'
        sh 'hostname'
        sh 'cd api;pytest -v --cov'
      }
    }
  }
}