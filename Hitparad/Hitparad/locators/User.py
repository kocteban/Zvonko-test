from selenium.webdriver.common.by import By
from random import *


class UserLocators:
    VK_AUTH = (By.CSS_SELECTOR, "._98._99")
    YA_AUTH = (By.CSS_SELECTOR, "._98._9c")
    MAIL_AUTH = (By.CSS_SELECTOR, "._98._9a")
    LOGOUT = (By.CSS_SELECTOR, "._f7 a")
    USER_ACC = (By.CSS_SELECTOR, "._91")

    n = randint(1, 100)
    LIKE_RANDOM_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[%s]/div[4]/div"
                         % n)
    RANDOM_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[%s]" % n)

    USER_SONGS = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/a[1]")
    USER_ALBUMS = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]")
    USER_PLAYLIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/a[3]")
    USER_COLLECTION = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/a[4]")
    USER_SINGERS = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/a[5]")

    FIRST_COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li/a/span")

    CREATE_PLAYLIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/a")
    REMOVE_PLAYLIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div")
    REMOVE_PLAYLIST_CONFIRM = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[4]/div/div/a")
    PLAYLIST_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div")
    EXIST_PLAYLIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[2]/a/div/div/img")
    FIRST_TRACK_PLAYLIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/div/li")

    PLAYLIST_SEARCH = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/form/div/div/div/input")
    CONFIRM_SEARCH = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/form/div/div/div/div/button")
    FIRST_SEARCH_TRACK = (By.CSS_SELECTOR, "div.searchPlaylist_popup > li:nth-child(1)")

    ADD_TRACK_TO_PLAYLIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[4]/div[1]")
    TRACK_CREATE_PLAYLIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[4]/div[1]/div/div")
    FIRST_ELEMENT_IN_LIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[4]/div[1]/div/ul/li")