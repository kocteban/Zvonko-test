from random import *
from selenium.webdriver.common.by import By


class GenresPageLocators:
    n = randint(1, 12)
    k = randrange(2, 5, 2)
    GENRE_NAME = (By.CSS_SELECTOR, ".span.desktop>:nth-child(1)>ul:nth-child(%s)>:nth-child(%s) a" % (k, n))
