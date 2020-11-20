pipeline {
  agent { docker { image 'alivx/urless'} }
  stages {
    stage('test') {
      steps {
        sh 'cd /api/;pytest'
      }
    }
    stage('Done') {
      steps {
        sh 'echo Done'
      }
    }
  }
}