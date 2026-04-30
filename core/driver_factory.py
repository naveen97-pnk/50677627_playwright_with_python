from selenium import webdriver
from config.env import Env

def get_driver():
    if Env.BROWSER == "chrome":
        options = webdriver.ChromeOptions()
        if Env.HEADLESS == "True":
            options.add_argument("--headless")
        driver = webdriver.Chrome(options)
    else:
        raise Exception("Browser not supported")
    driver.maximize_window()
    driver.implicitly_wait(Env.TIMEOUT)
    return driver



