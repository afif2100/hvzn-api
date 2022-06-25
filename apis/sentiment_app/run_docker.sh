#bin/bash
export REGISTRY=asia.gcr.io/hvzn-development/afif2100/sentiment-app

# if build
# if [ $1 "BUILD" ]
# then
docker build --no-cache -t ${REGISTRY}:latest .
# if push
docker push ${REGISTRY}:latest
# if run
# docker run -d -p 8000:8000 ${REGISTRY}:latest 