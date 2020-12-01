pipeline {
  agent any
  stages {
    stage('Fluffy Build') {
      steps {
        sh 'echo "ali bd98bc09-c458-4ea8-9880-1e871e0b7d5b"'
      }
    }
    stage('Fluffy Test') {
      parallel {
        stage('Backend') {
          steps {
            sh 'echo "ali 8009a9d8-d503-4661-a11b-f495ab287580"'
          }
        }
        stage('Frontend') {
          steps {
            sh 'echo "ali 4ba01100-cc21-423e-8f85-d6390cbaefde"'
          }
        }
        stage('Performance') {
          steps {
            sh 'echo "ali 61c9aa85-ddb9-4c5a-a5ae-bcce65d30ec2"'
          }
        }
        stage('Static') {
          steps {
            sh 'echo "ali bb72e33c-b6b0-45c0-a8f7-05d438ecf6ef"'
          }
        }
      }
    }
    stage('Fluffy Deploy') {
      steps {
        sh 'echo "ali 07eee196-fa9d-41b3-8b35-5ca7cfe87a2a"'
      }
    }
  }
}