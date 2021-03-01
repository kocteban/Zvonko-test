from selenium.webdriver.common.by import By


class MenuLocators:
    MENU_RADIO = (By.CSS_SELECTOR, "div.mH20.mH5p > ul > li:nth-child(1) > a")
    MENU_GENRES = (By.CSS_SELECTOR, "div.mH20.mH5p > ul > li:nth-child(2) > a")
    MENU_SINGERS = (By.CSS_SELECTOR, "div.mH20.mH5p > ul > li:nth-child(3) > a")
    MENU_ALBUMS = (By.CSS_SELECTOR, "div.mH20.mH5p > ul > li:nth-child(4) > a")
    MENU_COLLECTIONS = (By.CSS_SELECTOR, "div.mH20.mH5p > ul > li:nth-child(5) > a")
