import pytest
from conftest import *
from hrmpages.loginpage import LoginPage
@pytest.mark.usefixtures("launch_browser")
class TestLoginPage:


    def  setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page=LoginPage(self.driver)
    def test_valid_login(self):
        self.login_page.login(email,password)
    def teardown_class(self):
        self.driver.quit()