import time
import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from untilities.readProperties import ReadConfig
from untilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("**** Test_SearchCustomerByName_004 *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful ******")

        self.logger.info("***** Starting Search Customer By Name ")

        self.addCus = AddCustomer(self.driver)
        self.addCus.clickOnCustomersMenu()
        self.addCus.clickOnCustomerSubMenu()

        self.logger.info("**** Searching Customer By NameId *****")
        searchCus = SearchCustomer(self.driver)
        searchCus.setFirstName("Victoria")
        searchCus.setLastName("Terces")
        searchCus.clickSearch()
        time.sleep(5)
        status = searchCus.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("***** Finished *****")
        self.driver.close()
