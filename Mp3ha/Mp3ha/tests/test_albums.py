import pytest
from modules import MainPage
from modules import SortPages
from modules import Menu
from helper import page_helper
from locators.Sort import *
from locators.BasePage import *
from locators.User import *
from locators.SingersAlbums import *
from modules import SingersAlbums


class TestAlbums:
    @pytest.mark.smoke
    def test_albums_name(self, browser):
        Menu.go_to_menu_albums(browser)
        name1 = page_helper.get_text_element(browser, *SingersAlbumsLocators.COLLECTION_NAME)
        SingersAlbums.open_random_collection(browser)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    @pytest.mark.regression
    def test_albums_sorting(self, browser):
        Menu.go_to_menu_albums(browser)
        SortPages.press_second_sort(browser)
        name1 = page_helper.get_class_element(browser, *SortLocators.SECOND_SORT)
        name2 = SortLocators.ACTIVE_SORT
        assert name1 == name2

    @pytest.mark.smoke
    def test_albums_listen_button(self, browser):
        Menu.go_to_menu_albums(browser)
        SingersAlbums.open_random_collection(browser)
        MainPage.click_listen_button(browser)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    @pytest.mark.smoke
    def test_albums_like_button(self, browser):
        Menu.go_to_menu_albums(browser)
        SingersAlbums.open_random_collection(browser)
        MainPage.like_track(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.VK_AUTH)

    @pytest.mark.smoke
    def test_albums_favorite_button(self, browser):
        Menu.go_to_menu_albums(browser)
        SingersAlbums.open_random_collection(browser)
        MainPage.press_fav_button(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.VK_AUTH)
