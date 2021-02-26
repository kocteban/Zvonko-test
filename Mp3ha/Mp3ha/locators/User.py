from selenium.webdriver.common.by import By
from random import *


class UserLocators:
    VK_AUTH = (By.CSS_SELECTOR, ".mH48.mH49")
    YA_AUTH = (By.CSS_SELECTOR, ".mH48.mH4c")
    MAIL_AUTH = (By.CSS_SELECTOR, ".mH48.mH4a")
    LOGOUT = (By.CSS_SELECTOR, ".mHa [rel = 'nofollow']")
    USER_ACC = (By.CSS_SELECTOR, ".mH3y")

    n = randint(1, 100)
    LIKE_RANDOM_TRACK = (By.CSS_SELECTOR, " div.mH7l.mH7n > div > ul > li:nth-child(%s) > div.mH6d.mH6e"
                         % n)
    RANDOM_TRACK = (By.CSS_SELECTOR, "div.mH7l.mH7n > div > ul > li:nth-child(%s)" % n)

    USER_SONGS = (By.CSS_SELECTOR, ".mH3l.mH3k > :nth-child(1)")
    USER_ALBUMS = (By.CSS_SELECTOR, ".mH3l.mH3k > :nth-child(2)")
    USER_PLAYLIST = (By.CSS_SELECTOR, ".mH3l.mH3k > :nth-child(3)")
    USER_COLLECTION = (By.CSS_SELECTOR, ".mH3l.mH3k > :nth-child(4)")
    USER_SINGERS = (By.CSS_SELECTOR, ".mH3l.mH3k > :nth-child(5)")

    FIRST_COLLECTION_NAME = (By.CSS_SELECTOR, "div.mH7l.mH7n.mH7m > div > ul > li > a > span")

    CREATE_PLAYLIST = (By.CSS_SELECTOR, ".mH3q")
    REMOVE_PLAYLIST = (By.CSS_SELECTOR, ".mH77")
    REMOVE_PLAYLIST_CONFIRM = (By.CSS_SELECTOR, ".mH7f")
    PLAYLIST_NAME = (By.CSS_SELECTOR, ".mH6y > div")
    EXIST_PLAYLIST = (By.CSS_SELECTOR, ".mH6o img")
    FIRST_TRACK_PLAYLIST = (By.CSS_SELECTOR, "#mH79 li")

    PLAYLIST_SEARCH = (By.CSS_SELECTOR, ".mH64 .mH5d #mH65")
    CONFIRM_SEARCH = (By.CSS_SELECTOR, "#user-playlist-search button")
    FIRST_SEARCH_TRACK = (By.CSS_SELECTOR, ".mH67 > li:nth-child(1)")

    ADD_TRACK_TO_PLAYLIST = (By.CSS_SELECTOR, ".mH6a")
    TRACK_CREATE_PLAYLIST = (By.CSS_SELECTOR, ".mH6h")
    FIRST_ELEMENT_IN_LIST = (By.CSS_SELECTOR, "#list > li")