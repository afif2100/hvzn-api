#bin/bash
export REGISTRY=asia.gcr.io/hvzn-development/afif2100/sentiment-app


# if build
docker build --no-cache -t ${REGISTRY}:latest .
# if push
docker push ${REGISTRY}:latest
# if run