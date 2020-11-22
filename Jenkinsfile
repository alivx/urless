#!groovy
node {
    try {
        stage 'Checkout'
            checkout scm
            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            echo 'Start'
        stage 'Test'
            sh 'cd api;nosetests'
        stage 'Test'
            sh 'docker build . -t alivx/urless:latest'
        stage 'Publish results'
            echo 'DOne'
    }

    catch (err) {
        echo 'Error'

        throw err
    }

}