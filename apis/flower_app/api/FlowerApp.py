from asyncio.log import logger
from pickle import TRUE
import falcon
import tensorflow as tf
import numpy as np
from helper.base_logger import BaseLogger
import requests
from io import BytesIO
from PIL import Image
import numpy as np
import time
import os

log = BaseLogger(__name__)


class FlowerPrediction(object):
    def __init__(self) -> None:
        gpus = tf.config.experimental.list_physical_devices('GPU')
        for gpu in gpus:
            # set memory growth
            tf.config.experimental.set_memory_growth(gpu, True)

        self.model_location = "model/"
        self.loaded = False

        # Parameters
        self.input_size = (160, 160)
        self.channel = (3,)
        self.input_shape = self.input_size + self.channel

        # define labels
        self.labels = ["daisy", "dandelion", "rose", "sunflower", "tulip"]

        if not self.loaded:
            self.load()

    def load(self):
        self.model = tf.keras.models.load_model(self.model_location)
        self.loaded = True

        log.info("OK! Model Loaded")

    def preprocess(self, img, input_size):
        nimg = img.convert("RGB").resize(input_size, resample=0)
        img_arr = (np.array(nimg)) / 255
        return img_arr

    def _read_process(self, path):
        im = self._image_downloader(path)
        X = self.preprocess(im, self.input_size)
        
        # Reshape
        X = np.stack([X], axis=0)
        return X

    def _image_downloader(self, url):

        if os.environ["IMAGE_DEBUG"]:
            im = Image.open("example/img.jpg")
        else:
            im = Image.open(requests.get(url, stream=True).raw)
        return im

    def on_post(self, req, resp):
        # get json / dict payload
        # ref : https://falcon.readthedocs.io/en/stable/api/request_and_response_wsgi.html#id1
        input_payload = req.get_media()

        # get name from input
        path = input_payload.get("url", None)

        # preprocess image
        img = self._read_process(path)

        # set output payload
        t0 = time.time()
        y = self.model.predict(img, verbose=0)
        t1 = time.time() - t0

        label = self.labels[np.argmax(y)]
        score = np.max(y)
        payload = {"flowers": f"{label}", "score": f"{score}", "Prediction time": round(t1,4)}

        # send response
        # ref: https://falcon.readthedocs.io/en/stable/api/request_and_response_wsgi.html#response
        resp.status = falcon.HTTP_200
        resp.media = payload
        log.info(f"Status :{resp.status}, Prediction time : {t1}")
