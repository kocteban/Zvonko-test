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


def try_to_test_player_shuffle_repeat(browser, class_shuffle_or_repeat, n):
	browser.find_element_by_css_selector('.fixedBottom .play').click()
	track_name = browser.find_element_by_css_selector(".module-layout > .mainSongs > :nth-child(%s)" % n).get_attribute('data-id')
	browser.find_element_by_css_selector(class_shuffle_or_repeat).click()
	browser.find_element_by_css_selector('.next').click()
	next_track = browser.find_element_by_css_selector('.item.played.active').get_attribute('data-id')
	if n == 1:
		assert track_name == next_track
	else:
		assert track_name != next_track

