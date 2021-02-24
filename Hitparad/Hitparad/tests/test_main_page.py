import pytest
from urllib.parse import unquote
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

    @pytest.mark.smoke
    def test_main_page_sber_play(self, browser):
        MainPage.press_sber_play(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url

    @pytest.mark.regression
    def test_open_genres_list(self, browser):
        MainPage.open_genres_list(browser)
        assert page_helper.is_element_clickable(browser, *BasePageLocators.GENRES_LIST_GENRE)

    @pytest.mark.regression
    def test_open_random_genre(self, browser):
        MainPage.open_genres_list(browser)
        page_helper.get_text_element(browser, *BasePageLocators.RANDOM_GENRE_LIST)
        MainPage.open_random_genre(browser)
        name1 = page_helper.get_text_element(browser, *BasePageLocators.RANDOM_GENRE_LIST)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1, print(name1, h1)

    @pytest.mark.regression
    def test_main_page_description(self, browser):
        name1 = page_helper.get_text_element(browser, *BasePageLocators.ALPHABET_LETTER)
        MainPage.open_random_letter(browser)
        cur_url = unquote(browser.current_url)
        need_url = BasePageLocators.SITE_URL + "artists-index/%s" % name1
        assert cur_url == need_url
