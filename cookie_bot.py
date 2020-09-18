from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

DRIVER_PATH = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(DRIVER_PATH)

driver.get('https://orteil.dashnet.org/cookieclicker')

driver.implicitly_wait(5)   # the program waits here for 5 seconds so the page can fully load

cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')
cookie_producers = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1, -1, -1)]   # 3, 2, 1, 0

click_cookie_actions = ActionChains(driver)  # ActionChains performs queued actions
click_cookie_actions.click(on_element=cookie)

for _ in range(5000):
    click_cookie_actions.perform()   # clicking the cookie is performing constantly
    owned_cookies = int(cookie_count.text.split()[0])   # getting number of baked cookies

    for producer in cookie_producers:   # iterating over upgrades
        price = int(producer.text.replace(',', ''))     # getting individual price of every upgrade
        if price <= owned_cookies:                              # if got cookies for an upgrade
            upgrade_producer_actions = ActionChains(driver)     # new action chain for clicking on the upgrades
            upgrade_producer_actions.move_to_element(producer)  # enqueue: moving cursor to current upgrade
            upgrade_producer_actions.click()                    # enqueue: clicking on it
            upgrade_producer_actions.perform()                  # perform queued actions

