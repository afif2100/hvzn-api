import psycopg2
from common.base_logger import BaseLogger

logger = BaseLogger('postgress')


class PostgressConnection(object):

    def __init__(self):
        self.host = "localhost"
        self.user = "postgres"
        self.password = ""
        self.db= "postgres"
        self.port = 5432

    def connectdb(self):
        self.conn = psycopg2.connect(database="postgres",
                                     user=self.user,
                                     password=self.password,
                                     host=self.host,
                                     port=self.port)

    def check_connection(self):
        try:
            self.connectdb()
            self.conn.close()
            return True
        except Exception as e:
            logger.error(e)
            return False
