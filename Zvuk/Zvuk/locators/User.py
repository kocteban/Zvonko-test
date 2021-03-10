from selenium.webdriver.common.by import By
from random import *


class UserLocators:
    YA_AUTH = (By.CSS_SELECTOR, ".Z-t44.Z-t48")
    MAIL_AUTH = (By.CSS_SELECTOR, ".Z-t44.Z-t46")
    LOGOUT = (By.CSS_SELECTOR, ".Z-t4c > a")
    USER_ACC = (By.CSS_SELECTOR, ".Z-t3x")

    n = randint(1, 100)
    LIKE_RANDOM_TRACK = (By.CSS_SELECTOR, ".mainSongs > :nth-child(%s) .Z-t2q.Z-t1j"
                         % n)
    RANDOM_TRACK = (By.CSS_SELECTOR, ".mainSongs > :nth-child(%s)" % n)

    USER_SONGS = (By.CSS_SELECTOR, ".Z-t5i.Z-t4b > :nth-child(1)")
    USER_ALBUMS = (By.CSS_SELECTOR, ".Z-t5i.Z-t4b > :nth-child(2)")
    USER_PLAYLIST = (By.CSS_SELECTOR, ".Z-t5i.Z-t4b > :nth-child(3)")
    USER_COLLECTION = (By.CSS_SELECTOR, ".Z-t5i.Z-t4b > :nth-child(4)")
    USER_SINGERS = (By.CSS_SELECTOR, ".Z-t5i.Z-t4b > :nth-child(5)")

    FIRST_COLLECTION_NAME = (By.CSS_SELECTOR, "div.Z-t1a > ul > li > a > span")

    CREATE_PLAYLIST = (By.CSS_SELECTOR, ".Z-t6f")
    REMOVE_PLAYLIST = (By.CSS_SELECTOR, ".Z-t6y")
    REMOVE_PLAYLIST_CONFIRM = (By.CSS_SELECTOR, ".Z-t77")
    PLAYLIST_NAME = (By.CSS_SELECTOR, "div.Z-t6w > div")
    EXIST_PLAYLIST = (By.CSS_SELECTOR, ".Z-t6h > img")
    FIRST_TRACK_PLAYLIST = (By.CSS_SELECTOR, "#sortable li")

    PLAYLIST_SEARCH = (By.CSS_SELECTOR, ".Z-t1a .Z-t3e input")
    CONFIRM_SEARCH = (By.CSS_SELECTOR, ".Z-t1a .Z-t3e button")
    FIRST_SEARCH_TRACK = (By.CSS_SELECTOR, ".Z-t1h")

    ADD_TRACK_TO_PLAYLIST = (By.CSS_SELECTOR, ".Z-t1h")
    TRACK_CREATE_PLAYLIST = (By.CSS_SELECTOR, ".Z-t1q")
    FIRST_ELEMENT_IN_LIST = (By.CSS_SELECTOR, "#Z-t5n > li")