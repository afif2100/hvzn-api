#bin/bash
export REGISTRY=asia.gcr.io/hvzn-development/afif2100/falcon-app


# if build
docker build -t ${REGISTRY}:latest .
# if push
docker push ${REGISTRY}:latest
# if run