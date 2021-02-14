from selenium.webdriver.common.by import By
from random import *


class BottomCollectionLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, 'div.footerContent > div > div > ul:nth-child(%s) > li:nth-child(%s) > a > span'
                       % (str(randint(1, 8)), str(randint(2, 4))))

    HEADER = (By.CSS_SELECTOR, "div.footerContent > div > div > ul:nth-child(%s) > a" % str(randint(1, 8)))
