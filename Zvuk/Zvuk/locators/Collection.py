from selenium.webdriver.common.by import By
from random import *


class CollectionLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.Z-t7a > div:nth-child(%s) > div > div.Z-t4y.kinetic-active > ul > li:nth-child(3) > a > span" % str(randint(3, 24)))

    COLLECTION_SLIDER_HEADER = (By.CSS_SELECTOR, "div.span.Z-t7a > div:nth-child(%s) > h3 > a" % str(randint(3, 24)))

    k = randrange(3, 24)
    COLLECTION_SLIDER_ARROW = (By.CSS_SELECTOR, "div.span.Z-t7a > div:nth-child(%s) > div > div.Z-t4x" % k)
    COLLECTION_SLIDER_CHECK = (By.CSS_SELECTOR, "div.span.Z-t7a > div:nth-child(%s) div.Z-t4y.kinetic-active li:nth-child(5) span"
                               % k)