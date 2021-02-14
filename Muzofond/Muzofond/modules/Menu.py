from helper.page_helper import js_click
from locators.Menu import MenuLocators


def go_to_menu_news(browser):
	js_click(browser, *MenuLocators.TOP_MENU_NEWS)


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


def go_to_bot_menu_news(browser):
	js_click(browser, *MenuLocators.BOT_MENU_NEWS)


def go_to_bot_menu_genres(browser):
	js_click(browser, *MenuLocators.BOT_MENU_GENRES)


def go_to_bot_menu_singers(browser):
	js_click(browser, *MenuLocators.BOT_MENU_SINGERS)


def go_to_bot_menu_albums(browser):
	js_click(browser, *MenuLocators.BOT_MENU_ALBUMS)


def go_to_bot_menu_radio(browser):
	js_click(browser, *MenuLocators.BOT_MENU_RADIO)


def go_to_bot_menu_collections(browser):
	js_click(browser, *MenuLocators.BOT_MENU_COLLECTIONS)
