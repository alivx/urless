if [[ $1 == setup ]]; then
    virtualenv venv --distribute
    . venv/bin/activate
    cd api
    pip install -r requirements.txt
elif [[ $1 == test ]]; then
    cd api
    nosetests
fi
