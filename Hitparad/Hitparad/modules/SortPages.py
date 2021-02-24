from helper.page_helper import js_click
from locators.Sort import SortLocators


def press_first_sort(browser):
	js_click(browser, *SortLocators.FIRST_SORT)


def press_second_sort(browser):
	js_click(browser, *SortLocators.SECOND_SORT)
