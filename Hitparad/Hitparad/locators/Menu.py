from selenium.webdriver.common.by import By


class MenuLocators:
    TOP_MENU_NEWS = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/ul/li[1]/a")
    TOP_MENU_GENRES = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/ul/li[2]/a")
    TOP_MENU_SINGERS = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/ul/li[3]/a")
    TOP_MENU_ALBUMS = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/ul/li[4]/a")
    TOP_MENU_RADIO = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/ul/li[5]/a")
    TOP_MENU_COLLECTIONS = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/ul/li[6]/a")

    BOT_MENU_NEWS = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/ul/li[1]/a")
    BOT_MENU_GENRES = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/ul/li[2]/a")
    BOT_MENU_SINGERS = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/ul/li[3]/a")
    BOT_MENU_ALBUMS = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/ul/li[4]/a")
    BOT_MENU_RADIO = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/ul/li[5]/a")
    BOT_MENU_COLLECTIONS = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/ul/li[6]/a")