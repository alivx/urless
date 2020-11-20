pipeline {
  agent { docker { image 'python:3.7.2'} }
  stages {
    stage('build') {
      steps {
        sh 'useradd jenkins --shell /bin/bash --create-home;
        pip install -r api/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'cd api;pytest -v --cov'
      }
    }
  }
}