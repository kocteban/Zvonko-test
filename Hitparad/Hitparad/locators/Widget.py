from selenium.webdriver.common.by import By
from random import randint


class WidgetsLocators:
    POPULAR_SHOW_ALL = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/h3/a")
    SINGERS_SHOW_ALL = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[3]/h3/a")
    RADIO_SHOW_ALL = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[4]/h3/a")
    SPORT_SHOW_ALL = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[5]/h3/a")
    OST_SHOW_ALL = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[6]/h3/a")
    GAMES_SHOW_ALL = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[7]/h3/a")
    NATIONAL_SHOW_ALL = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[8]/h3/a")

    POPULAR_COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/span[%s]/a" % randint(1, 15))
    SINGERS_COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[3]/span[%s]/a" % randint(1, 15))
    RADIO_COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[4]/span[%s]/a" % randint(1, 15))
    SPORT_COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[5]/span[%s]/a" % randint(1, 15))
    OST_COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[6]/span[%s]/a" % randint(1, 15))
    GAMES_COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[7]/span[%s]/a" % randint(1, 15))
    NATIONAL_COLLECTION_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[8]/span[%s]/a" % randint(1, 15))
