from helper.page_helper import js_click
from locators.Menu import MenuLocators


def go_to_menu_genres(browser):
	js_click(browser, *MenuLocators.TOP_MENU_GENRES)


def go_to_menu_singers(browser):
	js_click(browser, *MenuLocators.TOP_MENU_SINGERS)


def go_to_menu_albums(browser):
	js_click(browser, *MenuLocators.TOP_MENU_ALBUMS)


def go_to_menu_radio(browser):
	js_click(browser, *MenuLocators.TOP_MENU_RADIO)


def go_to_menu_collections(browser):
	js_click(browser, *MenuLocators.TOP_MENU_COLLECTIONS)
