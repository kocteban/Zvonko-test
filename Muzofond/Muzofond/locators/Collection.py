from selenium.webdriver.common.by import By
from random import *


class CollectionLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, "div.kineticCenter.kinetic-active > ul > li:nth-child(%s) > a > span" % str(randint(1, 10)))

    n = randrange(2, 41, 2)
    COLLECTION_SLIDER_HEADER = (By.CSS_SELECTOR, "div.span.desktop > div > h3:nth-child(%s) > a" % n)

    k = randrange(3, 42, 2)
    COLLECTION_SLIDER_ARROW = (By.CSS_SELECTOR, "div.span.desktop > div > div:nth-child(%s) > div.kineticRight" % k)
    COLLECTION_SLIDER_CHECK = (By.CSS_SELECTOR, "div.span.desktop > div > div:nth-child(%s) > div.kineticCenter.kinetic-active > ul > li:nth-child(7) > a"
                               % k)