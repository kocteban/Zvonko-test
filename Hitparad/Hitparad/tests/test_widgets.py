import time
import pytest
from modules import Widgets
from helper import page_helper
from locators.Widget import *
from locators.BasePage import *


@pytest.mark.smoke
class TestWidgets:
    def test_widget_popular_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.POPULAR_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "сборники"

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
        assert h1 == "радио хиты"

    def test_widget_sport_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.SPORT_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "спортивная музыка"

    def test_widget_ost_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.OST_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "ost к фильмам и сериалам"

    def test_widget_games_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.GAMES_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "cаундтреки к играм"

    def test_widget_national_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.NATIONAL_SHOW_ALL)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "национальная музыка"

    def test_widget_popular_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.POPULAR_COLLECTION_NAME)
        page_helper.js_click(browser, *WidgetsLocators.POPULAR_COLLECTION_NAME)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_singers_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.SINGERS_COLLECTION_NAME)
        page_helper.js_click(browser, *WidgetsLocators.SINGERS_COLLECTION_NAME)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_radio_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.RADIO_COLLECTION_NAME)
        page_helper.js_click(browser, *WidgetsLocators.RADIO_COLLECTION_NAME)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_sport_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.SPORT_COLLECTION_NAME)
        page_helper.js_click(browser, *WidgetsLocators.SPORT_COLLECTION_NAME)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_ost_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.OST_COLLECTION_NAME)
        page_helper.js_click(browser, *WidgetsLocators.OST_COLLECTION_NAME)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_games_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.GAMES_COLLECTION_NAME)
        page_helper.js_click(browser, * WidgetsLocators.GAMES_COLLECTION_NAME)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_national_collection(self, browser):
        name1 = page_helper.get_text_element(browser, *WidgetsLocators.NATIONAL_COLLECTION_NAME)
        page_helper.js_click(browser, *WidgetsLocators.NATIONAL_COLLECTION_NAME)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    def test_widget_news_play(self, browser):
        page_helper.js_click(browser, *WidgetsLocators.NEWS_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_widget_news_stop(self, browser):
        page_helper.js_click(browser, *WidgetsLocators.NEWS_PLAY_STOP)
        time.sleep(0.5)
        page_helper.js_click(browser, *WidgetsLocators.NEWS_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PAUSED_TRACK)
