from selenium.webdriver.common.by import By


class MenuLocators:
    TOP_MENU_GENRES = (By.CSS_SELECTOR, ".menu-box > :nth-child(1) > a")
    TOP_MENU_SINGERS = (By.CSS_SELECTOR, ".menu-box > :nth-child(2) > a")
    TOP_MENU_ALBUMS = (By.CSS_SELECTOR, ".menu-box > :nth-child(3) > a")
    TOP_MENU_RADIO = (By.CSS_SELECTOR, ".menu-box > :nth-child(4) > a")
    TOP_MENU_COLLECTIONS = (By.CSS_SELECTOR, ".menu-box > :nth-child(5) > a")

    BOT_MENU_GENRES = (By.CSS_SELECTOR, "div.backShadows.footerLeft > div > ul > li:nth-child(1) > a")
    BOT_MENU_SINGERS = (By.CSS_SELECTOR, "div.backShadows.footerLeft > div > ul > li:nth-child(2) > a")
    BOT_MENU_ALBUMS = (By.CSS_SELECTOR, "div.backShadows.footerLeft > div > ul > li:nth-child(3) > a")
    BOT_MENU_RADIO = (By.CSS_SELECTOR, "div.backShadows.footerLeft > div > ul > li:nth-child(4) > a")
    BOT_MENU_COLLECTIONS = (By.CSS_SELECTOR, "div.backShadows.footerLeft > div > ul > li:nth-child(5) > a")