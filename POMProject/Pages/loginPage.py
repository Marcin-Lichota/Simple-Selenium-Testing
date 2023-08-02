from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = "//input[@data-v-1f99f73c]"
        self.password_textbox_name = 'password'
        self.button_xpath = "//button[@data-v-10d463b7]"
        self.validation_message_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username).clear()
        self.driver.find_element(By.XPATH, self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_xpath).click()

    def check_message(self):
        message = self.driver.find_element(By.XPATH, self.validation_message_xpath).text
        return message
