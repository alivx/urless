#!groovy
node {
    try {
        agent { docker { image 'alivx/urless'} }
        stage 'Checkout'
            checkout scm
            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            echo 'Start'
        stage 'Setup'
            sh 'cd /api/;virtualenv env -p python'
            sh 'cd /api/;. env/bin/activate'
            sh 'cd /api/;pip install -r requirements.txt'
            sh 'cd /api/;nosetests'

        stage 'test'
            sh 'cd /api/;virtualenv env -p python'
            sh 'cd /api/;. env/bin/activate'
            sh 'cd /api/;nosetests'

        stage 'Publish results'
            echo 'DOne'
    }

    catch (err) {
        echo 'Error'

        throw err
    }

}