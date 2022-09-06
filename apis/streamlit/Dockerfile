FROM afif2100/docker-base:latest

USER $USER
COPY . $WORKDIR
COPY session-ahvzn21 /tmp/.instaloader-root/session-ahvzn21

RUN pip install -r requirements.txt
# ENV PORT=8000
# ENV STREAMLIT_SERVER_PORT=${PORT}

ENTRYPOINT [ "streamlit","run","Home.py"]