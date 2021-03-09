from selenium.webdriver.common.by import By


class WidgetsLocators:
    MONTH_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(6) > div > div.titleCollections > h3 > a")
    GENRES_SHOW_ALL = ()
    SINGERS_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(5) > h3 > a")
    POPULAR_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(4) > h3 > a")
    NEWS_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(4) > h3 > a")
    RADIO_ONLINE_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(7) > h3 > a")
    TOP_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(8) > h3 > a")
    TV_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(9) > h3 > a")
    RADIO_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(10) > h3 > a")
    EUROPE_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(11) > h3 > a")

    POPULAR_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(4) > span:nth-child(2) > a")
    SINGERS_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(5) > span:nth-child(2) > a")
    RADIO_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(7) > span:nth-child(2) > a")
    SPORT_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(8) > span:nth-child(2) > a")
    OST_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(9) > span:nth-child(2) > a")
    GAMES_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(10) > span:nth-child(2) > a")
    NATIONAL_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(11) > span:nth-child(2) > a")

    NEWS_PLAY_STOP = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(6) > div > div.module-layout > ul > li:nth-child(1)")
