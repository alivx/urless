pipeline {
  agent any
  stages {
    stage('URLess Setup') {
      steps {
        sh 'bash build.sh setup'
      }
    }
    stage('URLess Test') {
      steps {
        sh 'bash build.sh test'
      }
    }
    stage('URLess Zip') {
      steps {
              parallel (
                  "firstTask" : {
                            sh 'bash build.sh zip'

                  },
                  "secondTask" : {
                      sh "ls"
                  }
              )
          }
    }
    stage('URLess Archive') {
      steps {
        parallel{
        archiveArtifacts artifacts: 'ali.zip', fingerprint: true, followSymlinks: false, onlyIfSuccessful: true,
        sh "scp ali.zip root@172.31.113.171:/root/"

        }
      }
    }
  }
}