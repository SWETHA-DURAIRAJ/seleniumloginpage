from selenium.webdriver.common import by

from hrmhelper.selenium_helper import Selenium_Helper
from selenium.webdriver.common.by import By
class LoginPage(Selenium_Helper):
    email_webelement=(By.XPATH,"//*[@name='username']")
    pswd_webelement=(By.XPATH,"//*[@name='password']")
    login_button=(By.XPATH,"//*[@id='submit']")
    def __init__(self, driver):
        super().__init__(driver) # pass to call the constructor
    def login(self, email, password):
        self.webelement_enter(self.email_webelement,email)
        self.webelement_enter(self.pswd_webelement,password)
        self.webelement_click(self.login_button)