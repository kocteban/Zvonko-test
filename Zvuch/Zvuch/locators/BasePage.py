from selenium.webdriver.common.by import By
from random import *


class BasePageLocators:
    SITE_URL = 'https://test.mp3poisk.me/'

    PLAYING_TRACK = (By.CSS_SELECTOR, ".item.played.active")
    PAUSED_TRACK = (By.CSS_SELECTOR, ".item.played.active.pause")
    RANDOM_TRACK = (By.CSS_SELECTOR, ".mainSongs > :nth-child(%s)" % str(randint(1, 100)))
    FIRST_TRACK = (By.CSS_SELECTOR, ".mainSongs > :nth-child(1)")
    SECOND_TRACK = (By.CSS_SELECTOR, ".mainSongs > :nth-child(2)")
    PLAYING_RADIO = (By.CSS_SELECTOR, ".item.play")
    LISTEN_BUTTON = (By.CSS_SELECTOR, ".listen.button")
    PLAY_RANDOM_TRACK = (By.CSS_SELECTOR, ".module-layout .mainSongs>:nth-child(%s) .play" % str(randint(1, 100)))

    LIKE_TRACK = (By.CSS_SELECTOR, ".favorite.favoriteIco")
    BUTTON_FAVORITE = (By.CSS_SELECTOR, ".button.outline.favorite")

    PAGE_DESCRIPTION_NAME = (By.CSS_SELECTOR, "div.mobileHide.topPageDescription > p:nth-child(2) > a:nth-child(%s) > span"
                             % str(randint(2, 6)))

    SBER_PLAY_BUTTON = (By.CSS_SELECTOR, ".span.desktop .actions .playOther .playOtherLink")
    SBER_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, ".span.desktop .download .dl")
    SBER_URL = "sber-zvuk.com"

    H1 = 'body h1'

    MAIN_LOGO = (By.CSS_SELECTOR, ".large_screen")

    SEARCH = (By.CSS_SELECTOR, "#search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#inHeader [type = 'submit']")