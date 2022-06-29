#bin/bash
export REGISTRY=asia.gcr.io/hvzn-development/afif2100/sentiment-app
export TAG=latest

docker build --no-cache -t ${REGISTRY}:${TAG} .
docker push ${REGISTRY}:${TAG}


# if [[ $1  -eq  "build" ]]
# then
#     docker build --no-cache -t ${REGISTRY}:${TAG} .
# elif [[ $1  -eq "push" ]]
# then
#     docker push ${REGISTRY}:${TAG}
# fi