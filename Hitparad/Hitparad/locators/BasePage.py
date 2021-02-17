from selenium.webdriver.common.by import By
from random import *


class BasePageLocators:
    SITE_URL = 'https://top.hitparad.fm/'

    PLAYING_TRACK = (By.XPATH, ".item.played.active")
    PAUSED_TRACK = (By.XPATH, ".item.played.active.pause")
    PLAYING_RADIO = (By.XPATH, ".item.play")
    LISTEN_BUTTON = (By.XPATH, ".listen.button")
    RANDOM_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[%s]" % str(randint(1, 100)))
    FIRST_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]")
    SECOND_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[2]")
    PLAY_RANDOM_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[%s]/div[1]/ul/li" % str(randint(1, 100)))

    LIKE_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[4]/div")
    BUTTON_FAVORITE = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/span")


    SBER_PLAY_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[1]/ul/noindex/li/a")
    SBER_URL = "sber-zvuk.com"

    H1 = '/html/body/div[2]/div[1]/div[2]/div[2]/div/div/h1'

    MAIN_LOGO = (By.XPATH, "/html/body/div[1]/div/a")

    SEARCH = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/form/div/div/div/input")
    SEARCH_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/form/div/div/div/div/button")

    GENRES_SHOW_ALL = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/h3/span")
    GENRES_LIST_GENRE = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/ul/li[52]/a")
    RANDOM_GENRE_LIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/ul/li[%s]/a" % str(randint(1, 61)))

    j = randint(1, 2)
    k = randint(1, 28)
    ALPHABET_LETTER = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/div/div/ul[%s]/li[%s]/a" % (j, k))
