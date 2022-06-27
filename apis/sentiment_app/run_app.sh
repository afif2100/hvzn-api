#bin/bash
export PORT=8080

gunicorn app:app -b 0.0.0.0:${PORT} -t 240