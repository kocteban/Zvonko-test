from helper.page_helper import js_click
from locators.BasePage import BasePageLocators


def click_listen_button(browser):
	js_click(browser, *BasePageLocators.LISTEN_BUTTON)


def play_random_track(browser):
	js_click(browser, *BasePageLocators.PLAY_RANDOM_TRACK)


def like_track(browser):
	js_click(browser, *BasePageLocators.LIKE_TRACK)


def press_fav_button(browser):
	js_click(browser, *BasePageLocators.BUTTON_FAVORITE)


def press_sber_play(browser):
	js_click(browser, *BasePageLocators.SBER_PLAY_BUTTON)


def open_genres_list(browser):
	js_click(browser, *BasePageLocators.GENRES_SHOW_ALL)


def open_random_genre(browser):
	js_click(browser, *BasePageLocators.RANDOM_GENRE_LIST)


def open_random_letter(browser):
	js_click(browser, *BasePageLocators.ALPHABET_LETTER)
