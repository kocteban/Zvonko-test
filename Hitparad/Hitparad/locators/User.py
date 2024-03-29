from selenium.webdriver.common.by import By
from random import *


class UserLocators:
    VK_AUTH = (By.CSS_SELECTOR, "._wA4z._wA50")
    YA_AUTH = (By.CSS_SELECTOR, "._wA4z._wA53")
    MAIL_AUTH = (By.CSS_SELECTOR, "._wA4z._wA51")
    LOGOUT = (By.CSS_SELECTOR, "._wA84 a")
    USER_ACC = (By.CSS_SELECTOR, "._wA4s")

    n = randint(1, 100)
    LIKE_RANDOM_TRACK = (By.CSS_SELECTOR, "div.span._wA7h > div > ul > li:nth-child(%s) > div._wA3e > div._wA81._wA82"
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
    FIRST_TRACK_PLAYLIST = (By.CSS_SELECTOR, "#_wA6u li")

    PLAYLIST_SEARCH = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/form/div/div/div/input")
    CONFIRM_SEARCH = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/form/div/div/div/div/button")
    FIRST_SEARCH_TRACK = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[3]/li[1]")

    ADD_TRACK_TO_PLAYLIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[4]/div[1]")
    TRACK_CREATE_PLAYLIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[4]/div[1]/div/div")
    FIRST_ELEMENT_IN_LIST = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div[4]/div[1]/div/ul/li")