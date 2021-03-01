from selenium.webdriver.common.by import By


class BottomPlayerLocators:
    BOTTOM_PLAY = (By.CSS_SELECTOR, ".mH12")
    BOTTOM_PAUSE = (By.CSS_SELECTOR, ".mH13")
    BOTTOM_PREV = (By.CSS_SELECTOR, ".mH10")
    BOTTOM_NEXT = (By.CSS_SELECTOR, ".mH11")
    BOTTOM_REPEAT = (By.CSS_SELECTOR, ".mHx")
    BOTTOM_SHUFFLE = (By.CSS_SELECTOR, ".mHy")
    BOTTOM_MUTE = (By.CSS_SELECTOR, ".mH17")
    BOTTOM_ACTIVE_MUTE = (By.CSS_SELECTOR, ".mH17.mHz")
    BOTTOM_ACTIVE_REPEAT = (By.CSS_SELECTOR, ".mHx.mHz")
    BOTTOM_ACTIVE_SHUFFLE = (By.CSS_SELECTOR, ".mHy.mHz")