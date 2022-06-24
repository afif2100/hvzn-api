# from common.pg_conn import PostgressConnection
import falcon
from datetime import datetime
from common.base_logger import BaseLogger

# from common import RedisConnection, PostgressConnection
import os

log = BaseLogger(__name__)


class HealthCheck(object):
    def __init__(self):
        self.start_time = datetime.now()

    def health(self):
        """
        Function that give health status
        """
        now_time = datetime.now()
        delta_time = now_time - self.start_time
        db_check_enable = eval(os.environ.get("ENABLE_DB_CHECK", "False"))

        payload = {"message": "ok", "uptime": str(delta_time)}
        if db_check_enable:
            payload.update({"db": self._get_db_status()})
        return payload

    def _get_db_status(self):
        db_status = {}
        # db_status["redis"] = str(RedisConnection().check_connection())
        # db_status["postgress"] = str(PostgressConnection().check_connection())
        return db_status

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = self.health()
