pipeline {
  agent { docker { image 'alivx/urless'} }
  stages {
    stage('test') {
      steps {
        sh 'pytest -v --cov'
      }
    }
    stage('Done') {
      steps {
        sh 'echo Done'
      }
    }
  }
}