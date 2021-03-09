from selenium.webdriver.common.by import By


class SortLocators:
    FIRST_SORT = (By.CSS_SELECTOR, ".Z-t5i>:nth-child(1)")
    SECOND_SORT = (By.CSS_SELECTOR, ".Z-t5i>:nth-child(2)")
    ACTIVE_SORT = "Z-t5j"