pipeline {
  docker.image("alivx/urless").inside() {
    stage('Install dependencies') {
      sh 'pip install --upgrade pipenv && pipenv install --system --deploy'
    }

    stage('Run Test') {
      sh 'nosetests'
    }
  }
}
