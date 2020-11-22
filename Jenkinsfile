pipeline {
  agent { docker { image 'alivx/urless' } }
  docker.image("python:${args.python_version}").inside(docker_extra_params) {
    stage('Install dependencies') {
      sh 'pip install --upgrade pipenv && pipenv install --system --deploy'
    }

    stage('Run Test') {
      sh 'nosetests'
    }
  }
}
