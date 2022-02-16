import requests
import logging
import logging.config
from hole.fillin_list import GetList

logging.config.fileConfig("log/logging.conf")

logger = logging.getLogger(__name__)


class GetComment(GetList):
    def __init__(self, user_token, json):
        super().__init__(user_token=user_token)
        self.base_url = "https://pkuhelper.pku.edu.cn/services/pkuhole/api.php?"
        self.params["action"] = "getcomment"
        self.json = json

    def get_data(self):
        data = self.json
        pid = [i["pid"] for i in data if int(i["reply"]) > 0]
        data = []
        logger.debug(pid)
        for item in pid:
            data += self._get_data(p_key="pid", p_val=item)
        logger.info("Retrieved {} comments".format(len(data)))
        return data

    def _get_data(self, p_key, p_val):
        return super()._get_data(p_key, p_val, logger=logger)


if __name__ == "__main__":
    hole_list = GetList()
    data = hole_list._get_data()
    comments = GetComment(json=data)
    data = comments.get_data()
    # logger.info(data)
