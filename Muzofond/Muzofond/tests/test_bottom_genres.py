from helper.page_helper import js_click
from helper import page_helper
from locators.BottomGenres import *


class TestBottomCollections:
    def test_genres_collection_name(self, browser):
        name1 = page_helper.get_text_element(browser, *BottomCollectionLocators.COLLECTION_NAME)
        js_click(browser, *BottomCollectionLocators.COLLECTION_NAME)
        h1 = page_helper.get_h1_text(browser)
        assert name1 in h1
