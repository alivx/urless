getCommitIT() {
    echo ${BUILD_NUMBER}_$(git log --format="%h" -n 1)
}

if [[ $1 == build ]]; then
    docker build . -t alivx/urless:$(getCommitIT)
    docker build . -t alivx/urless:latest
elif [[ $1 == test ]]; then
    docker run --rm  alivx/urless:$(getCommitIT) test
elif [[ $1 == push ]]; then
    docker push alivx/urless:latest
elif [[ $1 == pull ]]; then
    docker pull alivx/urless:latest
elif [[ $1 == run ]]; then
    docker run --rm -d --name urless -p 8000:8000 alivx/urless:latest
    sleep 3
    docker stop urless
elif [[ $1 == noti ]]; then
    echo "Done"
fi
