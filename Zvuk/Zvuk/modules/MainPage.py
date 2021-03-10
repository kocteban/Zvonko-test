from helper.page_helper import js_click
from locators.BasePage import BasePageLocators


def click_page_description(browser):
	js_click(browser, *BasePageLocators.PAGE_DESCRIPTION_NAME)


def click_listen_button(browser):
	js_click(browser, *BasePageLocators.LISTEN_BUTTON)


def play_random_track(browser):
	js_click(browser, *BasePageLocators.PLAY_RANDOM_TRACK)


def like_track(browser):
	js_click(browser, *BasePageLocators.LIKE_TRACK)


def press_fav_button(browser):
	js_click(browser, *BasePageLocators.BUTTON_FAVORITE)


def press_sber_download(browser):
	js_click(browser, *BasePageLocators.SBER_DOWNLOAD_BUTTON)
