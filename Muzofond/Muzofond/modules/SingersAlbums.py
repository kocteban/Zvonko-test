from helper.page_helper import js_click
from locators.SingersAndAlbums import *


def open_random_collection(browser):
	js_click(browser, *SingerAndAlbumLocators.COLLECTION_NAME)