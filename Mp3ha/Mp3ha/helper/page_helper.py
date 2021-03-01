from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.BasePage import *


def press_button(browser, by, value):
    button = browser.find_element(by, value)
    button.click()


def get_text_element(browser, by, value):
    text1 = browser.find_element(by, value).text.lower()
    return text1


def is_element_present(browser, *element):
    try:
        browser.find_element(*element)
    except NoSuchElementException:
        return False
    return True


def is_not_element_present(browser, *element):
    try:
        WebDriverWait(browser, 4).until(EC.presence_of_element_located(element))
    except TimeoutException:
        return True
    return False


def is_element_displayed(browser, *element):
    try:
        WebDriverWait(browser, 4).until(EC.presence_of_element_located(*element))
    except TimeoutException:
        return False
    return True


def is_element_clickable(browser, *element):
    try:
        WebDriverWait(browser, 4).until(EC.element_to_be_clickable(element))
    except TimeoutException:
        return False
    return True


def is_not_element_clickable(browser, *element):
    try:
        WebDriverWait(browser, 4).until(EC.element_to_be_clickable(element))
    except TimeoutException:
        return True
    return False


def get_h1_text(browser):
    h1 = browser.find_element_by_css_selector(BasePageLocators.H1).text.lower()
    return h1


def switch_to_second_window(browser):
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)


def get_data_id(browser, by, value):
    data_id = browser.find_element(by, value).get_attribute('data-id')
    return data_id


def get_class_element(browser, by, value):
    class1 = browser.find_element(by, value).get_attribute('class')
    return class1


def input_words(browser, by, value, what):
    input_area = browser.find_element(by, value)
    input_area.send_keys(what)


def go_to_main_page(browser):
    js_click(browser, *BasePageLocators.MAIN_LOGO)


def js_click(browser, by, value):
    button = browser.find_element(by, value)
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)
    button.click()
