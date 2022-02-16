import requests
import logging
import logging.config

logging.config.fileConfig("log/logging.conf")

logger = logging.getLogger(__name__)


class GetList:
    def __init__(self, user_token, session: requests.Session()):
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
        self.session = session

    def __get(self):
        res = self.session.get(
            self.base_url,
            params=self.params,
            headers=self.header,
        )
        json_data = res.json()
        assert res.status_code == 200
        assert json_data["code"] == 0
        return json_data

    def __verify(self, data):
        tmp = data["data"]
        texts = [i["text"] for i in tmp if "text" in i]
        assert not all(["人机验证" in i for i in texts])
        return True

    def _get_data(self, p_key="p", p_val=1, logger=logger):
        self.params[p_key] = p_val
        json_data = self.__get()
        try:
            self.__verify(json_data)
        except AssertionError:
            logger.warning("need verify")
            header = {
                "user-agent": self.header["user-agent"],
                "referer": "https://www.google.com/",
            }
            r = self.session.get(
                "http://webcache.googleusercontent.com/search?q=cache:www.naukri.com/jobs-in-andhra-pradesh",
                headers=header,
            )
            assert r.status_code == 200
            json_data = self.__get()
            self.__verify(json_data)
        data = json_data["data"]
        logger.info("Retrieved {} holes".format(len(data)))
        return data

    def get_data(self, p_key="p", p_val=1):
        return self._get_data(p_key, p_val)
