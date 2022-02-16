from selenium import webdriver


def check(cookie: dict):
    driver = webdriver.Chrome()
    driver.get("https://pkuhelper.pku.edu.cn/hole/")
    for key, value in cookie.items():
        driver.add_cookie({"name": key, "value": value})
    driver.get("https://pkuhelper.pku.edu.cn/hole/")
    print(driver.get_cookies())
    driver.quit()


if __name__ == "__main__":
    check({"name": "value"})
