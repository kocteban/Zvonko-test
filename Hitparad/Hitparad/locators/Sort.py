from selenium.webdriver.common.by import By


class SortLocators:
    FIRST_SORT = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/span[1]")
    SECOND_SORT = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/span[2]")
    ACTIVE_SORT = "_f8"
