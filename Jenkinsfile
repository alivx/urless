pipeline {
  agent { docker { image 'alivx/urless'} }
  stages {
    stage('test') {
      steps {
        sh 'cd /api/;pytest -v --cov'
      }
    }
    stage('Done') {
      steps {
        sh 'echo Done'
      }
    }
  }
}