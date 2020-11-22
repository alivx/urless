#!groovy
node {
    try {
        stage 'Unit Test'
            sh 'cd api;nosetests'
        stage 'Dockerize'
            sh 'docker kill urless-dev && true || true'
            sh 'docker image rm alivx/urless:latest-dev'
            sh 'docker build . -t alivx/urless:latest-dev'
        stage 'API Test'
            sh 'docker run -d --rm --name urless-dev -p 8000:8000 alivx/urless:latest-dev uvicorn main:app'
            sh "curl --location --request POST 'http://127.0.0.1:8000/' \
                --header 'Content-Type: application/json' \
                --data-raw '{'url':'https://www.toptal.com/pfythonfv/buibld-hifgh-performing-apps-with-the-pfython--frfamework'}'"
            sh 'docker kill urless-dev && true || true'
        stage 'Publish results'
            echo 'DOne'
    }

    catch (err) {
        echo 'Error'

        throw err
    }

}