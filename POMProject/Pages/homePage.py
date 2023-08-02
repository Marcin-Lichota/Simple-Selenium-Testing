from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_class = 'oxd-userdropdown-name'
        self.logout_link_text = 'Logout'

    def click_welcome_link(self):
        self.driver.find_element(By.CLASS_NAME, self.welcome_link_class).click()

    def click_logout_link(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_text).click()
