FROM afif2100/docker-base

USER $USER
COPY . $WORKDIR

RUN pip install -r requirements.txt
ENV PORT=8080

CMD ["bash", "run_app.sh"]
