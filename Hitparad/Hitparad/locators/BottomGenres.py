from selenium.webdriver.common.by import By
from random import *


class BottomGenresLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, "div._wA1a._wA1h > ul > div:nth-child(%s) > li:nth-child(2) > a"
                       % str(randint(1, 8)))
