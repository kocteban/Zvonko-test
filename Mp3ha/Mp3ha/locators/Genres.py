from random import *
from selenium.webdriver.common.by import By


class GenresPageLocators:
    n = randint(1, 71)
    GENRE_NAME = (By.CSS_SELECTOR, "div.mH7l.mH7n > div > ul > li:nth-child(%s) > a > span" % n)
