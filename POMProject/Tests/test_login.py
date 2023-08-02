import os
import pytest
from selenium import webdriver
from POMProject.Pages import loginPage
from POMProject.Pages.homePage import HomePage

os.environ['PATH'] += r"C:\Users\Ja\chromedriver-win64"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5)


@pytest.fixture()
def login():
    login = loginPage.LoginPage(driver)
    return login


@pytest.fixture()
def home():
    home = HomePage(driver)
    return home


class TestLogin:

    def test_login_and_logout_test(self, login, home):
        login.enter_username('Admin')
        login.enter_password("admin123")
        login.click_login()
        home.click_welcome_link()
        home.click_logout_link()

    def test_failed_login(self, login):
        login.enter_username('a')
        login.enter_password("b")
        login.click_login()
        assert login.check_message() == "Invalid credentials"

    @classmethod
    def teardown_class(cls):
        driver.close()
        driver.quit()

# type 'pytest --html=report.html' to generate report
# if standalone pytest command won't work use python -m pytest
