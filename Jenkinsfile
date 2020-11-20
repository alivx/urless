pipeline {
  agent { docker { image 'python:3.7.2'} }
  stages {
    stage('build') {
      steps {
        sh 'pip install --no-cache-dir fastapi==0.61.2 redis==3.2.1 uvicorn==0.12.2 pytest'
      }
    }
    stage('test') {
      steps {
        sh 'cd api;pytest -v --cov'
      }
    }
  }
}