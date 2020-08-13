import pytest

from pageObjects.loginPage import LoginPage
from untilities.readProperties import ReadConfig
from untilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("*** Test_001_Login ***")
        self.logger.info("*** Verifying Home Page Title ***")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()

            self.logger.info("*** Home Page Title Is Passed ***")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\vkbora\\PycharmProjects\\nopcommerceApp\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()

            self.logger.error("*** Home Page Title Is Failed ***")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*** Verifying Login Test ***")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()

            self.logger.info("*** Login Test Is Passed ***")
            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\vkbora\\PycharmProjects\\nopcommerceApp\\Screenshots\\" + "test_login.png")
            self.driver.close()

            self.logger.error("*** Login Test Is Failed ***")
            assert False
