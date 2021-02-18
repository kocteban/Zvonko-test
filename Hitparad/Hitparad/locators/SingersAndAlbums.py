from selenium.webdriver.common.by import By
from random import *


class SingerAndAlbumLocators:
    COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[%s]/a/span" % randint(1, 100))