from random import *
from selenium.webdriver.common.by import By


class GenresPageLocators:
    n = randint(1, 71)
    GENRE_NAME = (By.CSS_SELECTOR, "div.span.desktop li:nth-child(%s) a span" % n)
    GENRE_ELEMENT = (By.CSS_SELECTOR, ".unstyled>.item")
    GENRE_DESCRIPTION = (By.CSS_SELECTOR, "div.item.main p > a:nth-child(%s) > span" % str(randint(1, 5)))