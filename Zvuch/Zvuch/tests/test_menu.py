from modules import Menu
from helper import page_helper


class TestMenu:
    def test_top_menu_genres(self, browser):
        Menu.go_to_menu_genres(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "жанры" == h1

    def test_top_menu_singers(self, browser):
        Menu.go_to_menu_singers(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "исполнители" == h1

    def test_top_menu_albums(self, browser):
        Menu.go_to_menu_albums(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "альбомы" == h1

    def test_top_menu_radio(self, browser):
        Menu.go_to_menu_radio(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "онлайн радио" == h1

    def test_top_menu_collections(self, browser):
        Menu.go_to_menu_collections(browser)
        url = browser.current_url
        needed_url = "https://wwv.zvuch.com/collections"
        assert needed_url == url

    def test_bot_menu_genres(self, browser):
        Menu.go_to_bot_menu_genres(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "жанры" == h1

    def test_bot_menu_singers(self, browser):
        Menu.go_to_bot_menu_singers(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "исполнители" == h1

    def test_bot_menu_albums(self, browser):
        Menu.go_to_bot_menu_albums(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "альбомы" == h1

    def test_bot_menu_radio(self, browser):
        Menu.go_to_bot_menu_radio(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "онлайн радио" == h1

    def test_bot_menu_collections(self, browser):
        Menu.go_to_bot_menu_collections(browser)
        url = browser.current_url
        needed_url = "https://wwv.zvuch.com/collections"
        assert needed_url == url
