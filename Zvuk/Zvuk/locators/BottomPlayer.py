from selenium.webdriver.common.by import By


class BottomPlayerLocators:
    BOTTOM_PLAY = (By.CSS_SELECTOR, ".Z-te")
    BOTTOM_PAUSE = (By.CSS_SELECTOR, ".Z-tf")
    BOTTOM_PREV = (By.CSS_SELECTOR, ".Z-tc")
    BOTTOM_NEXT = (By.CSS_SELECTOR, ".Z-td")
    BOTTOM_REPEAT = (By.CSS_SELECTOR, ".Z-tq")
    BOTTOM_SHUFFLE = (By.CSS_SELECTOR, ".Z-tr")
    BOTTOM_MUTE = (By.CSS_SELECTOR, ".Z-tm")
    BOTTOM_ACTIVE_MUTE = (By.CSS_SELECTOR, ".Z-tm .Z-tn")
    BOTTOM_ACTIVE_REPEAT = (By.CSS_SELECTOR, ".Z-tq .Z-tn")
    BOTTOM_ACTIVE_SHUFFLE = (By.CSS_SELECTOR, ".Z-tr .Z-tn")