from selenium.webdriver.common.by import By
from random import *


class BottomCollectionLocators:
    COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/ul/div[%s]/li[1]/a"
                       % str(randint(1, 8)))
