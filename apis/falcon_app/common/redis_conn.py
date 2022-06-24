import redis
from common.base_logger import BaseLogger
import os

logger = BaseLogger('redis')


class RedisConnection(object):

    def __init__(self):
        self.host = os.environ.get("REDIS_HOST", "localhost")
        self.user = os.environ.get("REDIS_USER", "")
        self.password = os.environ.get("REDIS_PASSWORD", "")
        self.port = int(os.environ.get("REDIS_PORT", 6379))

    def connectdb(self):
        self.red = redis.Redis(host=self.host,
                               username=self.user,
                               port=self.port,
                               password=self.password)

    def check_connection(self):
        try:
            self.connectdb()
            self.red.ping()
            db_ok = True
        except Exception as e:
            logger.error(e)
            db_ok = False

        return db_ok
