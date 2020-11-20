pipeline {
  agent { docker { image 'alivx/urless'} }
  stages {
    stage('test') {
      steps {
        sh 'cd /api/;ls;pytest --cov'
      }
    }
    stage('Done') {
      steps {
        sh 'echo Done'
      }
    }
  }
}