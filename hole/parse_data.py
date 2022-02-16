import logging
from hole.fillin_list import GetList
from hole.get_comment import GetComment
import time
from sqlalchemy import create_engine
import pandas as pd
import requests

engine = create_engine("sqlite:///hole.db")
engine.execute(
    """
CREATE VIEW IF NOT EXISTS dataforhuman AS
SELECT
  a.text AS DZ,
  b.text AS reply
FROM
  list a
  LEFT OUTER JOIN `comment` b on a.pid = b.pid
ORDER BY
  a.pid,
  b.timestamp;
"""
)

logging.config.fileConfig("log/logging.conf")

logger = logging.getLogger(__name__)


class App:
    def __init__(self, user_token, sleeptime=1):
        self.user_token = user_token
        self.sleep_time = sleeptime
        self.session = requests.Session()

    def run(self):
        hole_list = GetList(user_token=self.user_token, session=self.session)
        pval = 1
        hole_list_data = []
        for pval in range(1, 10):
            hole_list_data += hole_list.get_data(p_key="p", p_val=pval)
            logger.info("Get hole list data")
            logger.info(hole_list_data)
        hole_list_df = pd.DataFrame(hole_list_data)
        hole_list_df.to_sql("list", engine, if_exists="append", index=False)
        comment_list = GetComment(
            user_token=self.user_token, json=hole_list_data, session=self.session
        )
        comment_data = comment_list.get_data()
        comment_df = pd.DataFrame(comment_data)
        comment_df.to_sql("comment", engine, if_exists="append", index=False)
        logger.info(comment_data)
        time.sleep(self.sleep_time)
        hole_list = pd.read_sql("select * from list", engine)
        hole_list.drop_duplicates(subset=["pid"], inplace=True, keep="last")
        hole_list.to_sql("list", engine, if_exists="replace", index=False)
        comment = pd.read_sql("select * from comment", engine)
        comment.drop_duplicates(subset=["cid"], inplace=True, keep="last")
        comment.to_sql("comment", engine, if_exists="replace", index=False)

    def run_thread(self):
        logger.info("Start")
        while True:
            self.run()
