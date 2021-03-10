from locators.BottomPlayer import BottomPlayerLocators


def press_play_button(browser):
	browser.find_element(*BottomPlayerLocators.BOTTOM_PLAY).click()


def press_mute_button(browser):
	browser.find_element(*BottomPlayerLocators.BOTTOM_MUTE).click()


def press_shuffle_button(browser):
	browser.find_element(*BottomPlayerLocators.BOTTOM_SHUFFLE).click()


def press_repeat_button(browser):
	browser.find_element(*BottomPlayerLocators.BOTTOM_REPEAT).click()


def press_pause_button(browser):
	browser.find_element(*BottomPlayerLocators.BOTTOM_PAUSE).click()


def press_prev_button(browser):
	browser.find_element(*BottomPlayerLocators.BOTTOM_PREV).click()


def press_next_button(browser):
	browser.find_element(*BottomPlayerLocators.BOTTOM_NEXT).click()
