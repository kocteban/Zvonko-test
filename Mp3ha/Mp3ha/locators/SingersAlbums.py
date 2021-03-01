from random import *
from selenium.webdriver.common.by import By


class SingersAlbumsLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, "div.mH7l.mH7n > div > ul > li:nth-child(%s) > a:nth-child(1) > div > img"
                       % randint(1, 50))
