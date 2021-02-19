from selenium.webdriver.common.by import By
from random import *


class BasePageLocators:
    SITE_URL = 'https://top.hitparad.fm/'

    PLAYING_TRACK = (By.CSS_SELECTOR, "._wA3._wAt")
    PAUSED_TRACK = (By.CSS_SELECTOR, "._wA3._wAt._wAl")
    LISTEN_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/a")
    RANDOM_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[%s]" % str(randint(1, 100)))
    FIRST_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]")
    SECOND_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[2]")
    PLAY_RANDOM_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[%s]/div[1]/ul/li" % str(randint(1, 100)))

    LIKE_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[4]/div")
    BUTTON_FAVORITE = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/span")

    SBER_PLAY_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[1]/ul/noindex/li/a")
    SBER_URL = "sber-zvuk.com"

    H1 = (By.CSS_SELECTOR, '._wA14 h1')

    MAIN_LOGO = (By.XPATH, "/html/body/div[1]/div/a")

    SEARCH = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/form/div/div/div/input")
    SEARCH_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/form/div/div/div/div/button")

    GENRES_SHOW_ALL = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/h3/span")
    GENRES_LIST_GENRE = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/ul/li[52]/a")
    RANDOM_GENRE_LIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/ul/li[%s]/a" % str(randint(1, 61)))

    j = randint(1, 2)
    k = randint(1, 28)
    ALPHABET_LETTER = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/div/div/ul[%s]/li[%s]/a" % (j, k))
