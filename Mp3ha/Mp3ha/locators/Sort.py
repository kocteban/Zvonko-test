from selenium.webdriver.common.by import By


class SortLocators:
    FIRST_SORT = (By.CSS_SELECTOR, ".mH3l>:nth-child(1)")
    SECOND_SORT = (By.CSS_SELECTOR, ".mH3l>:nth-child(2)")
    ACTIVE_SORT = ".mH3m"
