import pytest
from helper import page_helper
from modules import MainPage
from locators.BasePage import *
from locators.User import *


class TestMainPage:
    @pytest.mark.smoke
    def test_main_page_play(self, browser):
        MainPage.play_random_track(browser)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    @pytest.mark.smoke
    def test_main_page_like(self, browser):
        MainPage.like_track(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.VK_AUTH)
