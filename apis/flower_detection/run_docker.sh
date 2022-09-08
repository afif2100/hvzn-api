#!/bin/sh
export PROJECT_ID=hvzn-development
export REPO_NAME=afif2100
export IMAGE_NAME=flower-app
export IMAGE_TAG=latest
# export IMAGE_URI=asia.gcr.io/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}
export IMAGE_URI=${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}


echo "doker $1 : ${IMAGE_URI}"

if [ "$1" == "build" ]; then
    docker build --rm -t ${IMAGE_URI} . 
elif [ "$1" == "run" ]; then
    # docker run -it -p 9000:8000 --gpus all --rm ${IMAGE_URI} $2
    docker run -it -p 9001:9000 --rm ${IMAGE_URI} $2
elif [ "$1" == "push" ]; then
    docker push ${IMAGE_URI}
elif [ "$1" == "pull" ]; then
    docker pull ${IMAGE_URI}
elif [ "$1" == "bash" ]; then
    docker run --rm -it --gpus all --entrypoint bash ${IMAGE_URI}
else
    echo "try again"
fi