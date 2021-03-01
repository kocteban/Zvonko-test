from selenium.webdriver.common.by import By


class RadioLocators:
    OPEN_RADIO = (By.CSS_SELECTOR, "div.mH7l.mH7n > div > ul > li:nth-child(3)")
    RADIO_PLAY = (By.CSS_SELECTOR, "div.mH7l.mH7n > div > div.radio.mH4h > div > a")
    PLAYING_RADIO = (By.CSS_SELECTOR, ".mH74.mH3.mH75.mH12.mH16")