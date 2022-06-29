FROM afif2100/docker-base

USER $USER
COPY . $WORKDIR

RUN pip install -r requirements.txt
RUN python helper/model_download.py
ENV PORT=8000

CMD ["bash", "run_app.sh"]
