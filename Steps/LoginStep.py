from BaseTest import driver
from selenium.webdriver.common import by
from PageObject import LoginPage as loginPage

driver.find_element(by.By.XPATH(loginPage.username)).send_keys('Teste')

driver.quit()
