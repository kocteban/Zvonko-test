import pytest
from modules import Menu
from helper import page_helper


class TestMenu:
    @pytest.mark.smoke
    def test_menu_genres(self, browser):
        Menu.go_to_menu_genres(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "жанры" == h1

    @pytest.mark.smoke
    def test_menu_singers(self, browser):
        Menu.go_to_menu_singers(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "исполнители" == h1

    @pytest.mark.smoke
    def test_menu_albums(self, browser):
        Menu.go_to_menu_albums(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "альбомы" == h1

    @pytest.mark.smoke
    def test_menu_radio(self, browser):
        Menu.go_to_menu_radio(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "Радио-онлайн" == h1

    @pytest.mark.smoke
    def test_menu_collections(self, browser):
        Menu.go_to_menu_collections(browser)
        h1 = page_helper.get_h1_text(browser)
        assert "Сборники музыки" == h1