APP_FILE=app
IMAGE_NAME=gcr.io/fastapi-app/app
TAG=latest
PORT=8000

app:
	gunicorn $(APP_FILE):app -b 0.0.0.0:$(PORT) -k uvicorn.workers.UvicornWorker

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