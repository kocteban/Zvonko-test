from selenium.common.exceptions import NoSuchElementException
from helper.page_helper import js_click
from locators.BasePage import *
from locators.User import *


def login_user_acc(browser_cookies):
	browser_cookies.implicitly_wait(2)
	try:
		logout_user_acc(browser_cookies)
	except NoSuchElementException:
		pass
	go_to_user_acc(browser_cookies)
	js_click(browser_cookies, *UserLocators.YA_AUTH)


def logout_user_acc(browser_cookies):
	js_click(browser_cookies, *UserLocators.LOGOUT)


def like_random_track(browser_cookies):
	js_click(browser_cookies, *UserLocators.LIKE_RANDOM_TRACK)


def go_to_user_acc(browser_cookies):
	js_click(browser_cookies, *UserLocators.USER_ACC)


def unlike_first_track(browser_cookies):
	js_click(browser_cookies, *BasePageLocators.LIKE_TRACK)


def user_go_to_songs(browser_cookies):
	js_click(browser_cookies, *UserLocators.USER_SONGS)


def user_go_to_albums(browser_cookies):
	js_click(browser_cookies, *UserLocators.USER_ALBUMS)


def user_go_to_playlist(browser_cookies):
	js_click(browser_cookies, *UserLocators.USER_PLAYLIST)


def user_go_to_collection(browser_cookies):
	js_click(browser_cookies, *UserLocators.USER_COLLECTION)


def user_go_to_singers(browser_cookies):
	js_click(browser_cookies, *UserLocators.USER_SINGERS)


def create_new_playlist(browser_cookies):
	js_click(browser_cookies, *UserLocators.CREATE_PLAYLIST)


def go_to_exist_playlist(browser_cookies):
	js_click(browser_cookies, *UserLocators.EXIST_PLAYLIST)


def delete_playlist(browser_cookies):
	js_click(browser_cookies, *UserLocators.REMOVE_PLAYLIST)
	js_click(browser_cookies, *UserLocators.REMOVE_PLAYLIST_CONFIRM)


def create_music_playlist(browser_cookies):
	js_click(browser_cookies, *UserLocators.ADD_TRACK_TO_PLAYLIST)
	js_click(browser_cookies, *UserLocators.TRACK_CREATE_PLAYLIST)


def add_music_playlist(browser_cookies):
	js_click(browser_cookies, *UserLocators.ADD_TRACK_TO_PLAYLIST)
	js_click(browser_cookies, *UserLocators.FIRST_ELEMENT_IN_LIST)
