import time
import pytest
from modules import Carousels
from helper.page_helper import js_click
from helper import page_helper
from locators.Carousels import *
from locators.BasePage import *


@pytest.mark.smoke
class TestCarousels:
    def test_top_carousel_show_all_button(self, browser):
        js_click(browser, *CarouselsLocators.TOP_CAR_SHOW_ALL)
        cur_url = browser.current_url
        assert cur_url == BasePageLocators.SITE_URL + "collections/any"

    def test_mid_carousel_show_all_button(self, browser):
        js_click(browser, *CarouselsLocators.MID_CAR_SHOW_ALL)
        cur_url = browser.current_url
        assert cur_url == BasePageLocators.SITE_URL + "collections/ost"

    def test_bot_carousel_show_all_button(self, browser):
        js_click(browser, *CarouselsLocators.BOT_CAR_SHOW_ALL)
        url = browser.current_url
        assert url == BasePageLocators.SITE_URL + "collections/albums"

    def test_top_carousel_scroll_button(self, browser):
        Carousels.press_top_car_arrow(browser)
        assert page_helper.is_element_clickable(browser, *CarouselsLocators.TOP_COLLECTION)

    def test_mid_carousel_scroll_button(self, browser):
        Carousels.press_mid_car_arrow(browser)
        assert page_helper.is_element_clickable(browser, *CarouselsLocators.MID_COLLECTION)

    def test_bot_carousel_scroll_button(self, browser):
        Carousels.press_bot_car_arrow(browser)
        assert page_helper.is_element_clickable(browser, *CarouselsLocators.BOT_COLLECTION)

    @pytest.mark.xfail
    def test_top_carousel_open_collection(self, browser):
        Carousels.press_top_car_arrow(browser)
        name1 = page_helper.get_text_element(browser, *CarouselsLocators.TOP_COLLECTION_NAME)
        page_helper.press_button(browser, *CarouselsLocators.TOP_COLLECTION)
        name2 = page_helper.get_h1_text(browser)
        assert name1 == name2

    def test_mid_carousel_open_collection(self, browser):
        Carousels.press_mid_car_arrow(browser)
        name1 = page_helper.get_text_element(browser, *CarouselsLocators.MID_COLLECTION_NAME)
        page_helper.press_button(browser, *CarouselsLocators.MID_COLLECTION)
        name2 = page_helper.get_h1_text(browser)
        assert name1 == name2

    def test_bot_carousel_open_collection(self, browser):
        Carousels.press_bot_car_arrow(browser)
        name1 = page_helper.get_text_element(browser, *CarouselsLocators.BOT_COLLECTION_NAME)
        page_helper.press_button(browser, *CarouselsLocators.BOT_COLLECTION)
        name2 = page_helper.get_h1_text(browser)
        assert name1 == name2

    def test_top_carousel_scroll_back_button(self, browser):
        Carousels.press_top_car_arrow(browser)
        time.sleep(0.5)
        Carousels.press_top_car_back_arrow(browser)
        time.sleep(0.5)
        assert page_helper.is_not_element_clickable(browser, *CarouselsLocators.TOP_COLLECTION)

    def test_mid_carousel_scroll_back_button(self, browser):
        Carousels.press_mid_car_arrow(browser)
        time.sleep(0.5)
        Carousels.press_mid_car_back_arrow(browser)
        time.sleep(0.5)
        assert page_helper.is_not_element_clickable(browser, *CarouselsLocators.MID_COLLECTION)

    def test_bot_carousel_scroll_back_button(self, browser):
        Carousels.press_bot_car_arrow(browser)
        time.sleep(0.5)
        Carousels.press_bot_car_back_arrow(browser)
        time.sleep(0.5)
        assert page_helper.is_not_element_clickable(browser, *CarouselsLocators.BOT_COLLECTION)
