#bin/bash
export PORT=8000

gunicorn app:app -b 0.0.0.0:${PORT} -t 240