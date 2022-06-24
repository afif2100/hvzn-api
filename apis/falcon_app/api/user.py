from datetime import datetime, timedelta
from sqlalchemy import create_engine
import pandas as pd

class Users(object):

    def __init__(self):
        self.pg_host = "34.69.126.121:5432"
        self.pg_user = "postgres"
        self.pg_pass = "FarXCdD8HPe*CV2x=mH=74%sV$gK4BZXawWW!VQL"
        self.pg_db = "hvzn"
        self._conn_db()

    def _conn_db(self):
        self.engine = create_engine(
            f"postgresql+psycopg2://{self.pg_user}:{self.pg_pass}@{self.pg_host}/{self.pg_db}")

    def get_user(self):
        user = pd.read_sql(query, self.engine)
        return user



