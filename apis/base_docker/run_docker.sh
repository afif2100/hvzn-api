#bin/bash
export REGISTRY=afif2100/docker-base

# if build
docker build --no-cache -t ${REGISTRY}:latest .
# if push
docker push ${REGISTRY}:latest
# if run