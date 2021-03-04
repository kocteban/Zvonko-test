from selenium.webdriver.common.by import By
from random import *


class BasePageLocators:
    SITE_URL = 'https://music.zvuk.top/'

    PLAYING_TRACK = (By.CSS_SELECTOR, ".Z-t1b.Z-tn")
    PAUSED_TRACK = (By.CSS_SELECTOR, ".Z-t1b.Z-tn.Z-tf")
    RANDOM_TRACK = (By.CSS_SELECTOR, ".mainSongs > :nth-child(%s)" % str(randint(1, 100)))
    FIRST_TRACK = (By.CSS_SELECTOR, ".mainSongs > :nth-child(1)")
    SECOND_TRACK = (By.CSS_SELECTOR, ".mainSongs > :nth-child(2)")
    PLAYING_RADIO = (By.CSS_SELECTOR, ".Z-t1b.Z-te")
    LISTEN_BUTTON = (By.CSS_SELECTOR, ".Z-t2p.Z-t69")
    PLAY_RANDOM_TRACK = (By.CSS_SELECTOR, ".mainSongs>:nth-child(%s) .Z-te" % str(randint(1, 100)))

    LIKE_TRACK = (By.CSS_SELECTOR, ".Z-t2q.Z-t1j")
    BUTTON_FAVORITE = (By.CSS_SELECTOR, ".Z-t2q.Z-t7s")

    SBER_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, ".Z-tx")
    SBER_URL = "sber-zvuk.com"

    H1 = 'body h1'

    MAIN_LOGO = (By.CSS_SELECTOR, ".Z-t5")

    SEARCH = (By.CSS_SELECTOR, "#Z-t3g")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".form [type = 'submit']")
