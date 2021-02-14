from helper.page_helper import js_click
from locators.Carousels import CarouselsLocators


def press_show_all_top(browser):
	browser.find_element(*CarouselsLocators.TOP_CAR_SHOW_ALL).click()


def press_show_all_mid(browser):
	browser.find_element(*CarouselsLocators.MID_CAR_SHOW_ALL).click()


def press_show_all_bot(browser):
	browser.find_element(*CarouselsLocators.BOT_CAR_SHOW_ALL).click()


def press_top_car_arrow(browser):
	js_click(browser, *CarouselsLocators.TOP_CAR_ARROW)


def press_mid_car_arrow(browser):
	js_click(browser, *CarouselsLocators.MID_CAR_ARROW)


def press_bot_car_arrow(browser):
	js_click(browser, *CarouselsLocators.BOT_CAR_ARROW)


def press_top_car_back_arrow(browser):
	js_click(browser, *CarouselsLocators.TOP_CAR_BACK_ARROW)


def press_mid_car_back_arrow(browser):
	js_click(browser, *CarouselsLocators.MID_CAR_BACK_ARROW)


def press_bot_car_back_arrow(browser):
	js_click(browser, *CarouselsLocators.BOT_CAR_BACK_ARROW)
