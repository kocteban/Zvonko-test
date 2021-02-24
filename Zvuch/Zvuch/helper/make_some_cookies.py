from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Запись куки
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\python\Work\Zvonko-test\Zvuch\Zvuch\helper\selenium")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.zvuch.com/")
