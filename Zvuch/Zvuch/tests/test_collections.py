import time
import pytest
from modules import MainPage, Menu, Collections
from helper.page_helper import js_click
from helper import page_helper
from locators.Collection import *
from locators.BasePage import *
from locators.User import *

@pytest.mark.smoke
class TestCollections:
    def test_collections_carousel_show_all_button(self, browser):
        Menu.go_to_menu_collections(browser)
        name1 = page_helper.get_text_element(browser, *CollectionLocators.COLLECTION_SLIDER_HEADER)
        js_click(browser, *CollectionLocators.COLLECTION_SLIDER_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_collections_carousel_scroll_button(self, browser):
        Menu.go_to_menu_collections(browser)
        time.sleep(1)
        Collections.collection_scroll_carousel(browser)
        time.sleep(1)
        assert page_helper.is_element_clickable(browser, *CollectionLocators.COLLECTION_SLIDER_CHECK)

    def test_collections_carousel_open_collection(self, browser):
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

    def test_collections_sber_download_button(self, browser):
        Menu.go_to_menu_collections(browser)
        Collections.open_random_collection(browser)
        MainPage.press_sber_download(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url

    def test_collections_sber_play_button(self, browser):
        Menu.go_to_menu_collections(browser)
        Collections.open_random_collection(browser)
        MainPage.press_sber_play(browser)
        page_helper.switch_to_second_window(browser)
        cur_url = browser.current_url
        assert BasePageLocators.SBER_URL in cur_url

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
