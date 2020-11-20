pipeline {
  agent { docker { image 'alivx/urless'} }
  stages {
    stage('test') {
      steps {
        sh 'cd /api/;nosetests'
      }
    }
    stage('Done') {
      steps {
        sh 'echo Done'
      }
    }
  }
}