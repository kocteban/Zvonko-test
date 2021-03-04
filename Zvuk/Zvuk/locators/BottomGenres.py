from selenium.webdriver.common.by import By
from random import *


class BottomCollectionLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, "div.footerGenres > div.genres.boxShadow > ul > div:nth-child(%s) > li > a"
                       % str(randint(1, 8)))
