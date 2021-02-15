import time
import pytest
from modules import SortPages
from modules import Menu
from helper.page_helper import *
from helper import page_helper
from locators.Radio import *
from locators.BasePage import BasePageLocators


class TestRadio:
    @pytest.mark.smoke
    def test_radio_play(self, browser):
        Menu.go_to_menu_radio(browser)
        js_click(browser, *RadioLocators.RADIO_PLAY)
        time.sleep(3)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_RADIO)

    @pytest.mark.regression
    def test_radio_sorting(self, browser):
        Menu.go_to_menu_radio(browser)
        SortPages.press_second_sort(browser)
