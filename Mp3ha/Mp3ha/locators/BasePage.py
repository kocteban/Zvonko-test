from selenium.webdriver.common.by import By
from random import *


class BasePageLocators:
    SITE_URL = 'https://m.mp3ha.org/'

    PLAYING_TRACK = (By.CSS_SELECTOR, ".mH3.mHz")
    PAUSED_TRACK = (By.CSS_SELECTOR, ".mH3.mHz.mH13")
    RANDOM_TRACK = (By.CSS_SELECTOR, ".mH6f.mH0 > :nth-child(%s)" % str(randint(1, 100)))
    FIRST_TRACK = (By.CSS_SELECTOR, ".mH6f.mH0 > :nth-child(1)")
    SECOND_TRACK = (By.CSS_SELECTOR, ".mH6f.mH0 > :nth-child(2)")

    PLAY_RANDOM_TRACK = (By.CSS_SELECTOR, ".mH6f.mH0 > :nth-child(%s) .mH12" % str(randint(1, 100)))

    LIKE_TRACK = (By.CSS_SELECTOR, ".mH6d.mH6e")
    BUTTON_FAVORITE = (By.CSS_SELECTOR, ".mH74.mH7w.mH6d")

    LISTEN_BUTTON = (By.CSS_SELECTOR, ".mH74.mH75")

    H1 = 'body h1'

    MAIN_LOGO = (By.CSS_SELECTOR, ".mH9.mH8 img")

    SEARCH = (By.CSS_SELECTOR, "#mH65")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#main-search [type = 'submit']")