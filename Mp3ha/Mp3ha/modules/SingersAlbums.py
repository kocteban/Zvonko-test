from locators.SingersAlbums import *
from helper.page_helper import js_click


def open_random_collection(browser):
    js_click(browser, *SingersAlbumsLocators.COLLECTION_NAME)
