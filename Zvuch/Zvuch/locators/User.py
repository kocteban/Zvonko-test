from selenium.webdriver.common.by import By
from random import *


class UserLocators:
    VK_AUTH = (By.CSS_SELECTOR, ".authButton.vkauth")
    YA_AUTH = (By.CSS_SELECTOR, ".authButton.yandexauth")
    MAIL_AUTH = (By.CSS_SELECTOR, ".authButton.mailauth")
    LOGOUT = (By.CSS_SELECTOR, "body > div.header > div > div.logout > a")
    USER_ACC = (By.CSS_SELECTOR, ".myMusic")

    n = randint(1, 100)
    LIKE_RANDOM_TRACK = (By.CSS_SELECTOR, "div.span.desktop > div > ul > li:nth-child(%s) > div.itemRight > ul > li.favorite.favoriteIco"
                         % n)
    RANDOM_TRACK = (By.CSS_SELECTOR, "div.span.desktop > div > ul > li:nth-child(%s)" % n)

    USER_SONGS = (By.CSS_SELECTOR, "div.sort.favoritePage > :nth-child(1)")
    USER_ALBUMS = (By.CSS_SELECTOR, "div.sort.favoritePage > :nth-child(2)")
    USER_PLAYLIST = (By.CSS_SELECTOR, "div.sort.favoritePage > :nth-child(3)")
    USER_COLLECTION = (By.CSS_SELECTOR, "div.sort.favoritePage > :nth-child(4)")
    USER_SINGERS = (By.CSS_SELECTOR, "div.sort.favoritePage > :nth-child(5)")

    FIRST_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop > ul > li > a > span")

    CREATE_PLAYLIST = (By.CSS_SELECTOR, ".newPlaylist_cover")
    REMOVE_PLAYLIST = (By.CSS_SELECTOR, ".remove_playlist")
    REMOVE_PLAYLIST_CONFIRM = (By.CSS_SELECTOR, ".button_delete")
    PLAYLIST_NAME = (By.CSS_SELECTOR, "div.titlePlaylist > div")
    EXIST_PLAYLIST = (By.CSS_SELECTOR, "a.cover img")
    FIRST_TRACK_PLAYLIST = (By.CSS_SELECTOR, "#sortable li")

    PLAYLIST_SEARCH = (By.CSS_SELECTOR, ".span .inInputSearch input")
    CONFIRM_SEARCH = (By.CSS_SELECTOR, "#user-playlist-search > div > div.dropdown > button:nth-child(1)")
    FIRST_SEARCH_TRACK = (By.CSS_SELECTOR, "div.searchPlaylist_popup > li:nth-child(1)")

    ADD_TRACK_TO_PLAYLIST = (By.CSS_SELECTOR, ".inPlaylists")
    TRACK_CREATE_PLAYLIST = (By.CSS_SELECTOR, ".create_playlist")
    FIRST_ELEMENT_IN_LIST = (By.CSS_SELECTOR, "#list > li")