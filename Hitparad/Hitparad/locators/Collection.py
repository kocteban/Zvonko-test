from selenium.webdriver.common.by import By
from random import *


class CollectionLocators:
    COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[%s]/a/span" % str(randint(1, 10)))
