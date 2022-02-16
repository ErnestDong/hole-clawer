import requests
import logging
import logging.config

logging.config.fileConfig("log/logging.conf")

logger = logging.getLogger(__name__)


class GetList:
    def __init__(self, user_token):
        self.user_token = user_token
        self.base_url = "https://pkuhelper.pku.edu.cn/services/pkuhole/api.php"
        self.header = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "referer": "https://pkuhelper.pku.edu.cn/hole/",
        }

        self.params = {
            "action": "getlist",
            "PKUHelperAPI": "3.0",
            "user_token": self.user_token,
        }

    def _get_data(self, p_key="p", p_val=1, logger=logger):
        self.params[p_key] = p_val
        res = requests.get(
            self.base_url,
            params=self.params,
            headers=self.header,
        )
        json_data = res.json()
        assert res.status_code == 200
        assert json_data["code"] == 0
        try:
            tmp = json_data["data"]
            texts = [i["text"] for i in tmp if "text" in i]
            assert not all(["人机验证" in i for i in texts])
        except AssertionError:
            logger.warning("need verify")
            raise KeyError
        data = json_data["data"]
        logger.info("Retrieved {} holes".format(len(data)))
        return data

    def get_data(self, p_key="p", p_val=1):
        return self._get_data(p_key, p_val)


if __name__ == "__main__":
    hole = GetList()
    data = hole.get_data()
