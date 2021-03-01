from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators.BasePage import *

#Запись куки
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\python\Work\Zvonko-test\Mp3ha\Mp3ha\helper\selenium")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(BasePageLocators.SITE_URL)
