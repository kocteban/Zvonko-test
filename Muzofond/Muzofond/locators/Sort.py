from selenium.webdriver.common.by import By


class SortLocators:
    FIRST_SORT = (By.CSS_SELECTOR, ".sort>:nth-child(1)")
    SECOND_SORT = (By.CSS_SELECTOR, ".sort>:nth-child(2)")
    ACTIVE_SORT = "activated_sort"