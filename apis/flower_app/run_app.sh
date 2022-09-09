#bin/bash
export PORT=9000
# export IMAGE_DEBUG=True

gunicorn app:app -b 0.0.0.0:${PORT}