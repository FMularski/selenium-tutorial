from selenium import webdriver

DRIVER_PATH = 'C:\\chromedriver.exe'

driver = webdriver.Chrome(DRIVER_PATH)

driver.get('https://techwithtim.net')
print(driver.title)
driver.close()  # closes current tab
# driver.close()  # closes browser
