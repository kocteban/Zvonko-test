import pytest
from modules import Widgets
from helper.page_helper import *
from helper import page_helper
from locators.Widget import *
from locators.BasePage import *


@pytest.mark.smoke
class TestWidgets:
    def test_widget_news_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.NEWS_HEADER)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == 'новинки февраля 2021'

    def test_widget_ringtones_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.RINGTONES_HEADER)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "новинки рингтонов 2021"

    def test_widget_dj_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.DJ_HEADER)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "dj remix"

    def test_widget_hits_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.HITS_HEADER)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "золотые хиты 80-90-х"

    def test_widget_popular_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.POPULAR_HEADER)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "сборники новинок"

    def test_widget_radio_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.RADIO_HEADER)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "europa plus"

    def test_widget_tv_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.TV_HEADER)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "муз тв"

    def test_widget_vk_show_all(self, browser):
        Widgets.press_show_all_widgets(browser, *WidgetsLocators.VK_HEADER)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == "популярная музыка вк"

    def test_widget_news_play(self, browser):
        js_click(browser, *WidgetsLocators.NEWS_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_widget_ringtones_play(self, browser):
        js_click(browser, *WidgetsLocators.RINGTONES_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_widget_dj_play(self, browser):
        js_click(browser, *WidgetsLocators.DJ_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_widget_hits_play(self, browser):
        js_click(browser, *WidgetsLocators.HITS_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_widget_popular_play(self, browser):
        js_click(browser, *WidgetsLocators.POPULAR_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_widget_radio_play(self, browser):
        js_click(browser, *WidgetsLocators.RADIO_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_widget_tv_play(self, browser):
        js_click(browser, *WidgetsLocators.TV_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_widget_vk_play(self, browser):
        js_click(browser, *WidgetsLocators.VK_PLAY_STOP)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)
