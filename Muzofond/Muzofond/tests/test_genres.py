import time
import pytest
from modules import MainPage
from modules import Menu
from modules import Genres
from helper import page_helper
from locators.Genres import *
from locators.BasePage import *
from locators.User import *

@pytest.mark.smoke
class TestGenres:
    def test_genres_name(self, browser):
        Menu.go_to_menu_genres(browser)
        time.sleep(2)
        name1 = page_helper.get_text_element(browser, *GenresPageLocators.GENRE_NAME)
        Genres.open_random_genre(browser)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_genres_sber_play_button(self, browser):
        Menu.go_to_menu_genres(browser)
        time.sleep(2)
        Genres.open_random_genre(browser)
        time.sleep(2)
        MainPage.press_sber_play(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url

    def test_genres_sber_download_button(self, browser):
        Menu.go_to_menu_genres(browser)
        time.sleep(2)
        Genres.open_random_genre(browser)
        time.sleep(2)
        MainPage.press_sber_download(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url

    def test_genres_like_track_button(self, browser):
        Menu.go_to_menu_genres(browser)
        time.sleep(2)
        Genres.open_random_genre(browser)
        time.sleep(2)
        time.sleep(2)
        MainPage.like_track(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.VK_AUTH)
