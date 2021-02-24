from locators.Genres import *
from helper.page_helper import js_click
from random import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def count_genres(browser):
    amount_of_collections = browser.find_elements_by_css_selector(".box.filters [class = 'item collectionGrid']")
    n = len(amount_of_collections)
    n = randint(1, n)
    js_click(browser, By.CSS_SELECTOR, "div.span.desktop > div > ul > li:nth-child(%s) > a" % n)


def open_random_genre(browser):
    js_click(browser, *GenresPageLocators.GENRE_NAME)
    try:
        browser.implicitly_wait(2)
        count_genres(browser)
    except (NoSuchElementException, ValueError):
        pass
