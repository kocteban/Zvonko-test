import pytest
from modules import MainPage, Menu, Collections
from helper import page_helper
from locators.Collection import *
from locators.BasePage import *
from locators.User import *

@pytest.mark.smoke
class TestCollections:
    def test_collection_show_all(self, browser):
        Menu.go_to_menu_collections(browser)
        name1 = page_helper.get_text_element(browser, *CollectionLocators.COLLECTION_HEADER)
        Collections.collection_show_all(browser)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_collections_open_collection(self, browser):
        Menu.go_to_menu_collections(browser)
        name1 = page_helper.get_text_element(browser, *CollectionLocators.COLLECTION_NAME)
        Collections.open_random_collection(browser)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_collections_listen_button(self, browser):
        Menu.go_to_menu_collections(browser)
        Collections.open_random_collection(browser)
        MainPage.click_listen_button(browser)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_collections_like_button(self, browser):
        Menu.go_to_menu_collections(browser)
        Collections.open_random_collection(browser)
        MainPage.like_track(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.VK_AUTH)

    def test_collections_favorite_button(self, browser):
        Menu.go_to_menu_collections(browser)
        Collections.open_random_collection(browser)
        MainPage.press_fav_button(browser)
        assert page_helper.is_element_clickable(browser, *UserLocators.VK_AUTH)
