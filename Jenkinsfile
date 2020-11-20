pipeline {
  agent { docker { image 'python:3.7.2'} }
  stages {
    stage('build') {
      steps {
        sh '$(which hostname)'
        sh 'ls /var/log/'
        // sh 'pip install -r api/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh '$(which hostname)'
        sh 'ls /var/log/'
        sh 'cd api;pytest -v --cov'
      }
    }
  }
}