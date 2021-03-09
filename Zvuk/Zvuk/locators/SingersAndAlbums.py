from selenium.webdriver.common.by import By
from random import *


class SingerAndAlbumLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, ".Z-t4a > ul > li:nth-child(%s) > a > span" % randint(1, 100))