from selenium.webdriver.common.by import By


class WidgetsLocators:
    NEWS_HEADER = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(1) > div > h3 > a")
    RINGTONES_HEADER = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(2) > div > h3 > a")
    DJ_HEADER = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(3) > div > h3 > a")
    HITS_HEADER = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(4) > div > h3 > a")
    POPULAR_HEADER = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(5) > div > h3 > a")
    RADIO_HEADER = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(6) > div > h3 > a")
    TV_HEADER = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(7) > div > h3 > a")
    VK_HEADER = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(8) > div > h3 > a")

    NEWS_PLAY_STOP = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(1) > ul > li:nth-child(1) > div.mH27 > ul > span > div")
    RINGTONES_PLAY_STOP = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(2) > ul > li:nth-child(1) > div.mH27 > ul > span > div")
    DJ_PLAY_STOP = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(3) > ul > li:nth-child(1) > div.mH27 > ul > span > div")
    HITS_PLAY_STOP = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(4) > ul > li:nth-child(1) > div.mH27 > ul > span > div")
    POPULAR_PLAY_STOP = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(5) > ul > li:nth-child(1) > div.mH27 > ul > span > div")
    RADIO_PLAY_STOP = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(6) > ul > li:nth-child(1) > div.mH27 > ul > span > div")
    TV_PLAY_STOP = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(7) > ul > li:nth-child(1) > div.mH27 > ul > span > div")
    VK_PLAY_STOP = (By.CSS_SELECTOR, "div.mH7l.mH5m > div:nth-child(8) > ul > li:nth-child(1) > div.mH27 > ul > span > div")
