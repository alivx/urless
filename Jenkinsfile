#!groovy
node {
    try {
        stage 'Checkout'
            checkout scm
            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"

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
            slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
    }

    catch (err) {
        slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"

        throw err
    }

}