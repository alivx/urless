pipeline {
  agent { docker { image 'python:3.7.2'} }
  stages {
    stage('build') {
      steps {
        sh '$(which ifconfig)'
        sh '$(which hostname)'
        // sh 'pip install -r api/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh '$(which ifconfig)'
        sh '$(which hostname)'
        sh 'cd api;pytest -v --cov'
      }
    }
  }
}