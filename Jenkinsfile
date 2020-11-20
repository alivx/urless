pipeline {
  agent { docker { image 'alivx/urless'} }
  stages {
    stage('test') {
      steps {
        sh 'cd /api/;nose'
      }
    }
    stage('Done') {
      steps {
        sh 'echo Done'
      }
    }
  }
}