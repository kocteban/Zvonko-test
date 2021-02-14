from helper import page_helper
from helper.page_helper import *
from locators.BasePage import *


class TestSearch:
    def test_search(self, browser):
        page_helper.input_words(browser, *BasePageLocators.SEARCH, "привет")
        js_click(browser, *BasePageLocators.SEARCH_BUTTON)
        h1 = page_helper.get_h1_text(browser)
        assert h1 == 'привет'
