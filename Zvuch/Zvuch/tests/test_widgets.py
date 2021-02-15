import pytest
import time
from modules import Widgets
from helper.page_helper import *
from helper import page_helper
from locators.Widget import *
from locators.BasePage import *


@pytest.mark.smoke
class TestWidgets:
    def test_widget_genres_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.GENRES_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "жанры"

    def test_widget_singers_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.SINGERS_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "исполнители"

    def test_widget_news_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.NEWS_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "новинки"

    def test_widget_radio_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.RADIO_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "онлайн радио"

    def test_widget_ost_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.OST_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "ost к фильмам и сериалам"

    def test_widget_disco_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.DISCO_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "дискотека"

    def test_widget_national_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.NATIONAL_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "национальная музыка"

    def test_widget_genres_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.GENRES_COLLECTION_NAME)
        js_click(browser, *WidgetsLocators.GENRES_COLLECTION)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_singers_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.SINGERS_COLLECTION_NAME)
        js_click(browser, *WidgetsLocators.SINGERS_COLLECTION)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_ost_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.OST_COLLECTION_NAME)
        js_click(browser, *WidgetsLocators.OST_COLLECTION)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_disco_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.DISCO_COLLECTION_NAME)
        js_click(browser, *WidgetsLocators.DISCO_COLLECTION)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_national_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.NATIONAL_COLLECTION_NAME)
        js_click(browser, *WidgetsLocators.NATIONAL_COLLECTION)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_news_play(self, browser):
        js_click(browser, *WidgetsLocators.NEWS_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_widget_search_play(self, browser):
        js_click(browser, *WidgetsLocators.SEARCH_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_news_widget_stop(self, browser):
        js_click(browser, *WidgetsLocators.NEWS_PLAY_STOP)
        time.sleep(0.5)
        js_click(browser, *WidgetsLocators.NEWS_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PAUSED_TRACK)

    def test_widget_search_stop(self, browser):
        js_click(browser, *WidgetsLocators.SEARCH_PLAY_STOP)
        time.sleep(0.5)
        js_click(browser, *WidgetsLocators.SEARCH_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PAUSED_TRACK)

    def test_widget_news_singer_name(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.NEWS_SINGERS_NAME)
        js_click(browser, *WidgetsLocators.NEWS_SINGERS)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1, print(name1, h1)

    @pytest.mark.xfail
    def test_widget_news_track_name(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.NEWS_SONG_NAME)
        js_click(browser, *WidgetsLocators.NEWS_SONG)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1, print(name1, h1)

    def test_widget_search_track_name(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.SEARCH_SINGERS_NAME)
        js_click(browser, *WidgetsLocators.SEARCH_SINGER)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1, print(name1, h1)

    def test_widget_radio_play(self, browser):
        js_click(browser, *WidgetsLocators.RADIO_PLAY)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_RADIO)
