from hole.parse_data import App
import configparser
import sys
import logging

logging.disable(logging.INFO)
cmd = sys.argv
if len(cmd) == 3:
    user_token = cmd[2]
else:
    config = configparser.ConfigParser()
    config.read("config.ini")
    user_token = config["secrets"]["token"]

if __name__ == "__main__":
    app = App(user_token)
    # app.run()  # 跑一部分
    app.run_thread()  # 跑全部
