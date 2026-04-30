from ui.pages.login_page import LoginPage
from config.env import Env

def test_login(driver):
    login = LoginPage(driver)
    login.open(Env.UI_BASE_URL)
