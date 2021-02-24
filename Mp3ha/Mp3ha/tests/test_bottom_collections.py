import pytest
from helper.page_helper import js_click
from helper import page_helper
from locators.BottomCollection import *


class TestBottomCollections:
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_bottom_collection_header(self, browser):
        name1 = page_helper.get_text_element(browser, *BottomCollectionLocators.HEADER)
        js_click(browser, *BottomCollectionLocators.HEADER)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1

    @pytest.mark.regression
    def test_bottom_collection_name(self, browser):
        name1 = page_helper.get_text_element(browser, *BottomCollectionLocators.COLLECTION_NAME)
        js_click(browser, *BottomCollectionLocators.COLLECTION_NAME)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1
