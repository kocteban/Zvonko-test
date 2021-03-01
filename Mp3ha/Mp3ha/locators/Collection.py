from selenium.webdriver.common.by import By
from random import *


class CollectionLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, "div.mH7l.mH7n > div > div:nth-child(%s) > ul > li:nth-child(%s) > a:nth-child(2) > span"
                       % (str(randint(3, 16)), str(randint(1, 7))))

    n = randint(1, 16)
    COLLECTION_HEADER = (By.CSS_SELECTOR, "div.mH7l.mH7n > div > div:nth-child(%s) > h3 > a" % n)
    COLLECTION_SHOW_ALL = (By.CSS_SELECTOR, "div.mH7l.mH7n > div > div:nth-child(%s) > ul > li.mH57 > a" % n)
