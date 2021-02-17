from selenium.webdriver.common.by import By


class BottomPlayerLocators:
    BOTTOM_PLAY = (By.CSS_SELECTOR, ".group .play")
    BOTTOM_PAUSE = (By.CSS_SELECTOR, ".group .pause")
    BOTTOM_PREV = (By.CSS_SELECTOR, ".group .prev")
    BOTTOM_NEXT = (By.CSS_SELECTOR, ".group .next")
    BOTTOM_REPEAT = (By.CSS_SELECTOR, ".group .repeat")
    BOTTOM_SHUFFLE = (By.CSS_SELECTOR, ".group .shuffle")
    BOTTOM_MUTE = (By.CSS_SELECTOR, ".group .mute")
    BOTTOM_ACTIVE_MUTE = (By.CSS_SELECTOR, ".mute.active")
    BOTTOM_ACTIVE_REPEAT = (By.CSS_SELECTOR, ".repeat.active")
    BOTTOM_ACTIVE_SHUFFLE = (By.CSS_SELECTOR, ".shuffle.active")