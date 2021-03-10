from selenium.webdriver.common.by import By


class WidgetsLocators:
    MONTH_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(2) > a > div")
    GENRES_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(3) > a > div")
    COLLECTIONS_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(4) > a > div")
    SINGERS_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(5) > a > div")
    NEWS_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(6) > a > div")
    RADIO_ONLINE_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(7) > a > div")
    ALBUMS_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(8) > a > div")
    TOP_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(9) > a > div")
    TV_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(10) > a > div")
    RADIO_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(11) > a > div")
    EUROPE_SHOW_ALL = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(12) > a > div")

    GENRES_COLLECTION_NAME = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(3) > :nth-child(2) > :nth-child(1) span")
    COLLECTION_COLLECTION_NAME = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(4) > :nth-child(2) > :nth-child(1) span")
    SINGERS_COLLECTION_NAME = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(5) > :nth-child(2) > :nth-child(1) span")
    ALBUMS_COLLECTION_NAME = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(8) > :nth-child(2) > :nth-child(1) span")

    MONTH_PLAY = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(2) > a > div")
    NEWS_PLAY = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(6) li")
    RADIO_ONLINE_PLAY = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(7) li")
    TOP_PLAY = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(9) li")
    TV_PLAY = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(10) li")
    RADIO_PLAY = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(11) li")
    EUROPE_PLAY = (By.CSS_SELECTOR, ".Z-t3v > div:nth-child(12) li")
