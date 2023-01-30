APP_FILE=app

run:
	gunicorn $(APP_FILE):app -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker