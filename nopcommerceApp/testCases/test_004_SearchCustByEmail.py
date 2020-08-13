import time
import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from untilities.readProperties import ReadConfig
from untilities.customLogger import LogGen


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("**** Test_SearchCustomerByEmail_004 *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful ******")

        self.logger.info("***** Starting Search Customer By Email ")

        self.addCus = AddCustomer(self.driver)
        self.addCus.clickOnCustomersMenu()
        self.addCus.clickOnCustomerSubMenu()

        self.logger.info("**** Searching Customer By EmailId *****")
        searchCus = SearchCustomer(self.driver)
        searchCus.setEmail("victoria_victoria@nopCommerce.com")
        searchCus.clickSearch()
        time.sleep(5)
        status = searchCus.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("***** Finished *****")
        self.driver.close()
