#bin/bash

gunicorn app:app -b 0.0.0.0:${PORT} -t 240