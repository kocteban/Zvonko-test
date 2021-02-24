from selenium.webdriver.common.by import By


class BottomPlayerLocators:
    BOTTOM_PLAY = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]")
    BOTTOM_PAUSE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]")
    BOTTOM_PREV = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]")
    BOTTOM_NEXT = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]")
    BOTTOM_REPEAT = (By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]")
    BOTTOM_SHUFFLE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[2]")
    BOTTOM_MUTE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[3]")
    BOTTOM_ACTIVE_MUTE = (By.CSS_SELECTOR, "._wAh._wAt")
    BOTTOM_ACTIVE_REPEAT = (By.CSS_SELECTOR, "._wAs._wAt")
    BOTTOM_ACTIVE_SHUFFLE = (By.CSS_SELECTOR, "._wAu._wAt")