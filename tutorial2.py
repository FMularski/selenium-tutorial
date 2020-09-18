from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DRIVER_PATH = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(DRIVER_PATH)

driver.get('https://techwithtim.net')

link = driver.find_element_by_link_text('Python Programming')   # getting link element by its text
link.click()

try:
    beginner_tutorials_link = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials'))
    )

    beginner_tutorials_link.click()

    get_started_link = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'sow-button-19310003'))
    )
    get_started_link.click()

    driver.back()   # back in the browser
    driver.back()
    driver.back()

    driver.forward()    # forward in the browser
    driver.forward()

except:
    driver.quit()
