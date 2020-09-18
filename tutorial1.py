from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


DRIVER_PATH = 'C:\\chromedriver.exe'

driver = webdriver.Chrome(DRIVER_PATH)

driver.get('https://techwithtim.net')
print(driver.title)

search = driver.find_element_by_name('s')
search.clear()  # clears search field before sending keys
search.send_keys('test')
search.send_keys(Keys.RETURN)

# print(driver.page_source)  # printing all source code of the page

try:    # this try/finally code is used to wait for specific elements to be loaded ex. from the next subpage
    main = WebDriverWait(driver, 10).until(     # wait max 10 seconds
        ec.presence_of_element_located((By.ID, 'main'))
    )

    # print(main.text)  # printing text within main

    articles = main.find_elements_by_tag_name('article')  # returns a list of article elements
    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)

finally:
    driver.quit()
# main = driver.find_element_by_id('main')  # finding element by id


# driver.close()  # closes current tab
# driver.close()  # closes browser
