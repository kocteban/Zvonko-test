import pytest
from urllib.parse import unquote
from helper import page_helper
from modules import MainPage
from locators.BasePage import *
from locators.User import *


class TestMainPage:
    @pytest.mark.smoke
    def test_main_page_like(self, browser):
        MainPage.like_track(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.YA_AUTH)

    @pytest.mark.smoke
    def test_main_page_sber_download(self, browser):
        MainPage.press_sber_download(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url
