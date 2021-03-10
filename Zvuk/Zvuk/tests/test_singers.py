import pytest
from modules import MainPage
from modules import SortPages
from modules import Menu
from modules import SingersAlbums
from helper import page_helper
from locators.SingersAndAlbums import *
from locators.Sort import *
from locators.BasePage import *
from locators.User import *


class TestSingers:
    @pytest.mark.smoke
    def test_singers_name(self, browser):
        Menu.go_to_menu_singers(browser)
        name1 = page_helper.get_text_element(browser, *SingerAndAlbumLocators.COLLECTION_NAME)
        SingersAlbums.open_random_collection(browser)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    @pytest.mark.regression
    def test_singers_sorting(self, browser):
        Menu.go_to_menu_singers(browser)
        SortPages.press_second_sort(browser)
        name1 = page_helper.get_class_element(browser, *SortLocators.SECOND_SORT)
        name2 = SortLocators.ACTIVE_SORT
        assert name1 in name2

    @pytest.mark.smoke
    def test_singers_listen_button(self, browser):
        Menu.go_to_menu_singers(browser)
        SingersAlbums.open_random_collection(browser)
        MainPage.click_listen_button(browser)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    @pytest.mark.smoke
    def test_singers_sber_download_button(self, browser):
        Menu.go_to_menu_singers(browser)
        SingersAlbums.open_random_collection(browser)
        MainPage.press_sber_download(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url

    @pytest.mark.smoke
    def test_singers_like_button(self, browser):
        Menu.go_to_menu_singers(browser)
        SingersAlbums.open_random_collection(browser)
        MainPage.like_track(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.YA_AUTH)

    @pytest.mark.smoke
    def test_singers_favorite_button(self, browser):
        Menu.go_to_menu_singers(browser)
        SingersAlbums.open_random_collection(browser)
        MainPage.press_fav_button(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.YA_AUTH)
