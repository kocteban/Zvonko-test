import time
import pytest
from modules import Player
from helper import page_helper
from locators.BasePage import *
from locators.BottomPlayer import *


@pytest.mark.smoke
class TestPlayer:
    def test_play_button(self, browser):
        Player.press_play_button(browser)
        assert page_helper.is_element_present(browser, *BasePageLocators.PLAYING_TRACK)

    def test_pause_button(self, browser):
        Player.press_play_button(browser)
        Player.press_pause_button(browser)
        assert page_helper.is_element_present(browser, *BasePageLocators.PAUSED_TRACK)

    def test_mute_button(self, browser):
        Player.press_mute_button(browser)
        assert page_helper.is_element_present(browser, *BottomPlayerLocators.BOTTOM_ACTIVE_MUTE)

    def test_shuffle_button(self, browser):
        Player.press_shuffle_button(browser)
        assert page_helper.is_element_present(browser, *BottomPlayerLocators.BOTTOM_ACTIVE_SHUFFLE)

    def test_repeat_button(self, browser):
        Player.press_repeat_button(browser)
        assert page_helper.is_element_present(browser, *BottomPlayerLocators.BOTTOM_ACTIVE_REPEAT)

    def test_unmute_button(self, browser):
        Player.press_mute_button(browser)
        time.sleep(0.1)
        Player.press_mute_button(browser)
        assert page_helper.is_not_element_present(browser, *BottomPlayerLocators.BOTTOM_ACTIVE_MUTE)

    def test_next_track_button(self, browser):
        Player.press_play_button(browser)
        first_track = page_helper.get_data_id(browser, *BasePageLocators.PLAYING_TRACK)
        Player.press_next_button(browser)
        next_track = page_helper.get_data_id(browser, *BasePageLocators.PLAYING_TRACK)
        assert first_track != next_track

    def test_previous_track_button(self, browser):
        Player.press_play_button(browser)
        first_track = page_helper.get_data_id(browser, *BasePageLocators.PLAYING_TRACK)
        Player.press_next_button(browser)
        Player.press_prev_button(browser)
        next_track = page_helper.get_data_id(browser, *BasePageLocators.PLAYING_TRACK)
        assert first_track == next_track

    def test_repeat_track_button(self, browser):
        Player.press_play_button(browser)
        Player.press_repeat_button(browser)
        first_track = page_helper.get_data_id(browser, *BasePageLocators.PLAYING_TRACK)
        Player.press_next_button(browser)
        next_track = page_helper.get_data_id(browser, *BasePageLocators.PLAYING_TRACK)
        assert first_track == next_track

    def test_shuffle_track_button(self, browser):
        Player.press_play_button(browser)
        second_track = page_helper.get_data_id(browser, *BasePageLocators.SECOND_TRACK)
        Player.press_shuffle_button(browser)
        Player.press_next_button(browser)
        next_track = page_helper.get_data_id(browser, *BasePageLocators.RANDOM_TRACK)
        assert second_track != next_track
