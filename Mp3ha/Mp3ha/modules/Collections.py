from helper.page_helper import js_click
from locators.Collection import *


def open_random_collection(browser):
	js_click(browser, *CollectionLocators.COLLECTION_NAME)


def collection_show_all(browser):
	js_click(browser, *CollectionLocators.COLLECTION_SHOW_ALL)