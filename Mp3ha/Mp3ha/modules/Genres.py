from locators.Genres import *
from helper.page_helper import js_click


def open_random_genre(browser):
    js_click(browser, *GenresPageLocators.GENRE_NAME)