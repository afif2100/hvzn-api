import falcon
import json
from helper.base_logger import BaseLogger

log = BaseLogger(__name__)


class HelloName(object):
    def __init__(self):
        pass

    def on_post(self, req, resp):
        # get json / dict payload
        # ref : https://falcon.readthedocs.io/en/stable/api/request_and_response_wsgi.html#id1
        input_payload = req.get_media()

        # get name from input
        name = input_payload.get("name", None)

        # set output payload
        payload = {"msg": f"Hello, {name}!"}

        # send response
        # ref: https://falcon.readthedocs.io/en/stable/api/request_and_response_wsgi.html#response
        resp.status = falcon.HTTP_200
        resp.media = payload
