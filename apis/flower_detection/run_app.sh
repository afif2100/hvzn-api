#bin/bash
export PORT=9000

gunicorn app:app -b 0.0.0.0:${PORT}