from random import *
from selenium.webdriver.common.by import By


class GenresPageLocators:
    n = randint(1, 46)
    GENRE_NAME = (By.CSS_SELECTOR, "div.Z-t1a.Z-t36 > ul:nth-child(2) > div:nth-child(%s) > a > span" % n)
