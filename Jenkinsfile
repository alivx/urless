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
        parallel(
        "archive":{
          archiveArtifacts artifacts: 'ali.zip', fingerprint: true, followSymlinks: false, onlyIfSuccessful: true
        },
        "transfet":{
        sh "scp -o "StrictHostKeyChecking=no"   ali.zip root@172.31.113.171:/root/"
        }
        )
      }
    }
  }
}