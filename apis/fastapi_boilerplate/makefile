APP_FILE=app
# IMAGE_NAME=gcr.io/hvzn-development/fastapi-app/app
IMAGE_NAME=afif2100/fastapi-app
TAG=latest
PORT=8000

app:
	uvicorn $(APP_FILE):app --host 0.0.0.0 --port $(PORT) --reload --workers 10
# gunicorn $(APP_FILE):app -b 0.0.0.0:$(PORT) -k uvicorn.workers.UvicornWorker --reload

build:
	docker build -t $(IMAGE_NAME):$(TAG) .

push:
	docker push $(IMAGE_NAME):$(TAG)

run:
	docker run -it --rm -p $(PORT):$(PORT) $(IMAGE_NAME):$(TAG)

bash:
	docker run -it --rm $(IMAGE_NAME):$(TAG) bash

clean:
	docker rmi $(IMAGE_NAME):$(TAG)