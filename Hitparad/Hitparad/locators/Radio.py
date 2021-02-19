from selenium.webdriver.common.by import By

class RadioLocators:
    RADIO_PLAY = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[3]")
    PLAYING_RADIO = (By.CSS_SELECTOR, "._wA3._wAk")