import pytest
from modules import Menu
from modules import MainPage
from modules import SingersAlbums
from modules import Collections
from modules import User_acc
from helper.page_helper import *
from helper import page_helper
from locators.User import *
from locators.BasePage import *


@pytest.mark.smoke
class TestUserAcc:
    def test_user_auth(self, browser_cookies):
        User_acc.login_user_acc(browser_cookies)
        result = page_helper.is_element_clickable(browser_cookies, *UserLocators.LOGOUT)
        User_acc.logout_user_acc(browser_cookies)
        assert result

    def test_user_like_music(self, browser_cookies):
        User_acc.login_user_acc(browser_cookies)
        User_acc.like_random_track(browser_cookies)
        id1 = page_helper.get_data_id(browser_cookies, *UserLocators.RANDOM_TRACK)
        User_acc.go_to_user_acc(browser_cookies)
        id2 = page_helper.get_data_id(browser_cookies, *BasePageLocators.FIRST_TRACK)
        User_acc.unlike_first_track(browser_cookies)
        User_acc.logout_user_acc(browser_cookies)
        assert id1 == id2

    def test_user_like_albums(self, browser_cookies):
        User_acc.login_user_acc(browser_cookies)
        Menu.go_to_menu_albums(browser_cookies)
        SingersAlbums.open_random_collection(browser_cookies)
        name1 = page_helper.get_h1_text(browser_cookies)
        MainPage.press_fav_button(browser_cookies)
        User_acc.go_to_user_acc(browser_cookies)
        User_acc.user_go_to_albums(browser_cookies)
        name2 = page_helper.get_text_element(browser_cookies, *UserLocators.FIRST_COLLECTION_NAME)
        js_click(browser_cookies, *UserLocators.FIRST_COLLECTION_NAME)
        MainPage.press_fav_button(browser_cookies)
        User_acc.logout_user_acc(browser_cookies)
        assert name2 in name1

    def test_user_like_singers(self, browser_cookies):
        User_acc.login_user_acc(browser_cookies)
        Menu.go_to_menu_singers(browser_cookies)
        SingersAlbums.open_random_collection(browser_cookies)
        name1 = page_helper.get_h1_text(browser_cookies)
        MainPage.press_fav_button(browser_cookies)
        User_acc.go_to_user_acc(browser_cookies)
        User_acc.user_go_to_singers(browser_cookies)
        name2 = page_helper.get_text_element(browser_cookies, *UserLocators.FIRST_COLLECTION_NAME)
        js_click(browser_cookies, *UserLocators.FIRST_COLLECTION_NAME)
        MainPage.press_fav_button(browser_cookies)
        User_acc.logout_user_acc(browser_cookies)
        assert name2 in name1

    def test_user_like_collection(self, browser_cookies):
        User_acc.login_user_acc(browser_cookies)
        Menu.go_to_menu_collections(browser_cookies)
        Collections.open_random_collection(browser_cookies)
        name1 = page_helper.get_h1_text(browser_cookies)
        MainPage.press_fav_button(browser_cookies)
        User_acc.go_to_user_acc(browser_cookies)
        User_acc.user_go_to_collection(browser_cookies)
        name2 = page_helper.get_text_element(browser_cookies, *UserLocators.FIRST_COLLECTION_NAME)
        js_click(browser_cookies, *UserLocators.FIRST_COLLECTION_NAME)
        MainPage.press_fav_button(browser_cookies)
        User_acc.logout_user_acc(browser_cookies)
        assert name2 in name1

    def test_user_create_playlist(self, browser_cookies):
        User_acc.login_user_acc(browser_cookies)
        User_acc.go_to_user_acc(browser_cookies)
        User_acc.user_go_to_playlist(browser_cookies)
        User_acc.create_new_playlist(browser_cookies)
        name1 = page_helper.get_text_element(browser_cookies, *UserLocators.PLAYLIST_NAME)
        User_acc.delete_playlist(browser_cookies)
        User_acc.logout_user_acc(browser_cookies)
        assert name1 == 'новый плейлист'

    def test_user_add_new_music_playlist(self, browser_cookies):
        User_acc.login_user_acc(browser_cookies)
        User_acc.create_music_playlist(browser_cookies)
        id1 = page_helper.get_data_id(browser_cookies, *BasePageLocators.FIRST_TRACK)
        User_acc.go_to_user_acc(browser_cookies)
        User_acc.user_go_to_playlist(browser_cookies)
        User_acc.go_to_exist_playlist(browser_cookies)
        id2 = page_helper.get_data_id(browser_cookies, *UserLocators.FIRST_TRACK_PLAYLIST)
        User_acc.delete_playlist(browser_cookies)
        User_acc.logout_user_acc(browser_cookies)
        assert id1 == id2

    def test_user_search_music_in_playlist(self, browser_cookies):
        User_acc.login_user_acc(browser_cookies)
        User_acc.go_to_user_acc(browser_cookies)
        User_acc.user_go_to_playlist(browser_cookies)
        User_acc.create_new_playlist(browser_cookies)
        page_helper.input_words(browser_cookies, *UserLocators.PLAYLIST_SEARCH, "привет")
        js_click(browser_cookies, *UserLocators.CONFIRM_SEARCH)
        id1 = page_helper.get_data_id(browser_cookies, *UserLocators.FIRST_SEARCH_TRACK)
        js_click(browser_cookies, *UserLocators.ADD_TRACK_TO_PLAYLIST)
        id2 = page_helper.get_data_id(browser_cookies, *UserLocators.FIRST_TRACK_PLAYLIST)
        User_acc.delete_playlist(browser_cookies)
        User_acc.logout_user_acc(browser_cookies)
        assert id1 == id2

    def test_user_add_music_old_playlist(self, browser_cookies):
        User_acc.login_user_acc(browser_cookies)
        User_acc.go_to_user_acc(browser_cookies)
        User_acc.user_go_to_playlist(browser_cookies)
        User_acc.create_new_playlist(browser_cookies)
        page_helper.go_to_main_page(browser_cookies)
        User_acc.add_music_playlist(browser_cookies)
        id1 = page_helper.get_data_id(browser_cookies, *BasePageLocators.FIRST_TRACK)
        User_acc.go_to_user_acc(browser_cookies)
        User_acc.user_go_to_playlist(browser_cookies)
        User_acc.go_to_exist_playlist(browser_cookies)
        id2 = page_helper.get_data_id(browser_cookies, *UserLocators.FIRST_TRACK_PLAYLIST)
        User_acc.delete_playlist(browser_cookies)
        User_acc.logout_user_acc(browser_cookies)
        assert id1 == id2
