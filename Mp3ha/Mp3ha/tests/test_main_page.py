import pytest
from helper import page_helper
from modules import MainPage
from locators.BasePage import *
from locators.User import *


class TestMainPage:
    @pytest.mark.regression
    def test_main_page_description(self, browser):
        name1 = page_helper.get_text_element(browser, *BasePageLocators.PAGE_DESCRIPTION_NAME)
        MainPage.click_page_description(browser)
        name2 = page_helper.get_h1_text(browser)
        assert name1 in name2

    @pytest.mark.smoke
    def test_main_page_top_100_play_button(self, browser):
        MainPage.click_listen_button(browser)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    @pytest.mark.smoke
    def test_main_page_play(self, browser):
        MainPage.play_random_track(browser)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    @pytest.mark.smoke
    def test_main_page_like(self, browser):
        MainPage.like_track(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.VK_AUTH)

    @pytest.mark.smoke
    def test_main_page_sber_play(self, browser):
        MainPage.press_sber_play(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url

    @pytest.mark.smoke
    def test_main_page_sber_download(self, browser):
        MainPage.press_sber_download(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url
