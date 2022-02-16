import logging
from hole.fillin_list import GetList
from hole.get_comment import GetComment
import time


logging.config.fileConfig("log/logging.conf")

logger = logging.getLogger(__name__)


class App:
    def __init__(self, user_token, sleeptime=1):
        self.user_token = user_token
        self.sleep_time = sleeptime

    def run(self):
        hole_list = GetList(self.user_token)
        pval = 1
        for pval in range(1, 10):
            hole_list_data = hole_list.get_data(p_key="p", p_val=pval)
            logger.info(hole_list_data)
            comment_list = GetComment(self.user_token, hole_list_data)
            comment_data = comment_list.get_data()
            logger.info(comment_data)
        time.sleep(self.sleep_time)

    def run_thread(self):
        logger.info("Start")
        while True:
            self.run()


if __name__ == "__main__":
    app = App()
    app.run()
