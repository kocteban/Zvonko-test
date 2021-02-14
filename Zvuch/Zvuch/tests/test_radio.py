import time
from modules import SortPages
from modules import Menu
from helper.page_helper import *
from helper import page_helper
from locators.Radio import *


class TestRadio:
    def test_radio_play(self, browser):
        Menu.go_to_menu_radio(browser)
        js_click(browser, *RadioLocators.RADIO_PLAY)
        time.sleep(3)
        assert page_helper.is_element_present(browser, *RadioLocators.PLAYING_RADIO)

    def test_radio_sorting(self, browser):
        Menu.go_to_menu_radio(browser)
        SortPages.press_second_sort(browser)
