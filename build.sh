if [[ $1 == setup ]]; then
    virtualenv venv
    . venv/bin/activate
    cd api
    pip install -r requirements.txt
elif [[ $1 == test ]]; then
    . venv/bin/activate
    cd api
    nosetests
elif [[ $1 == zip ]]; then
    pwd
    zip -r ali.zip .
fi
