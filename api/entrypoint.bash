if [[ -z $1 ]]; then
    uvicorn main:app --host 0.0.0.0 --port ${port:-8080}
elif [[ $1 == test ]]; then
    cd /api
    nosetests
fi
