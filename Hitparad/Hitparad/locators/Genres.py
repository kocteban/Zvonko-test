from random import *
from selenium.webdriver.common.by import By


class GenresPageLocators:
    k = randrange(1, 2)
    n = randint(1, 13)
    GENRE_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul[%s]/div[%s]/li[1]/a" % (k, n))

