import pytest
from modules import MainPage
from modules import SortPages
from modules import Menu
from modules import Genres
from helper.page_helper import js_click
from helper import page_helper
from locators.Genres import *
from locators.Sort import *
from locators.BasePage import *
from locators.User import *


class TestGenres:
    @pytest.mark.smoke
    def test_genres_name(self, browser):
        Menu.go_to_menu_genres(browser)
        name1 = page_helper.get_text_element(browser, *GenresPageLocators.GENRE_NAME)
        Genres.open_random_genre(browser)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    @pytest.mark.regression
    def test_genres_sorting(self, browser):
        Menu.go_to_menu_genres(browser)
        SortPages.press_second_sort(browser)
        name1 = page_helper.get_class_element(browser, *SortLocators.SECOND_SORT)
        name2 = SortLocators.ACTIVE_SORT
        assert name1 in name2

    @pytest.mark.smoke
    def test_genres_listen_button(self, browser):
        Menu.go_to_menu_genres(browser)
        Genres.open_random_genre(browser)
        MainPage.click_listen_button(browser)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    @pytest.mark.smoke
    def test_genres_sber_play_button(self, browser):
        Menu.go_to_menu_genres(browser)
        Genres.open_random_genre(browser)
        MainPage.press_sber_play(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url

    @pytest.mark.smoke
    def test_genres_sber_download_button(self, browser):
        Menu.go_to_menu_genres(browser)
        Genres.open_random_genre(browser)
        MainPage.press_sber_download(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url

    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_genres_description(self, browser):
        Menu.go_to_menu_genres(browser)
        Genres.open_random_genre(browser)
        name1 = page_helper.get_text_element(browser, *GenresPageLocators.GENRE_DESCRIPTION)
        js_click(browser, *GenresPageLocators.GENRE_DESCRIPTION)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    @pytest.mark.smoke
    def test_genres_like_track_button(self, browser):
        Menu.go_to_menu_genres(browser)
        Genres.open_random_genre(browser)
        MainPage.like_track(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.VK_AUTH)
