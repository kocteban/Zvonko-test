from helper.page_helper import js_click
from locators.BasePage import BasePageLocators


def play_random_track(browser):
	js_click(browser, *BasePageLocators.PLAY_RANDOM_TRACK)


def like_track(browser):
	js_click(browser, *BasePageLocators.LIKE_TRACK)


def press_fav_button(browser):
	js_click(browser, *BasePageLocators.BUTTON_FAVORITE)


def click_listen_button(browser):
	js_click(browser, *BasePageLocators.LISTEN_BUTTON)
