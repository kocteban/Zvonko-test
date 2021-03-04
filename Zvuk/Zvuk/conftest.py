from selenium import webdriver
from locators.BasePage import BasePageLocators
import pytest


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(BasePageLocators.SITE_URL)
    yield browser
    browser.quit()


@pytest.fixture()
def browser_cookies():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("user-data-dir=C:\python\Work\Zvonko-test\Zvuk\Zvuk\helper\selen")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(BasePageLocators.SITE_URL)
    yield browser
    browser.quit()
