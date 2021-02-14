from selenium.webdriver.common.by import By

class RadioLocators:
    RADIO_PLAY = (By.CSS_SELECTOR, "div.span.desktop > div > ul > li:nth-child(3)")
    PLAYING_RADIO = (By.CSS_SELECTOR, ".item.collectionGrid.play")