from selenium.webdriver.common.by import By
from random import *


class BottomCollectionLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, 'div.mH1r > div > div > ul:nth-child(%s) > li:nth-child(%s) > a > span'
                       % (str(randint(1, 4)), str(randint(2, 6))))

    HEADER = (By.CSS_SELECTOR, "div.mH1r > div > div > ul:nth-child(%s) > a" % str(randint(1, 4)))
