import pytest
import time
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from untilities.readProperties import ReadConfig
from untilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("**** Test_003_AddCustomer ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.clickLogin()
        self.logger.info("**** Login Successful ****")
        self.logger.info("**** Add Customer Test ****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerSubMenu()

        self.addcust.clickOnAddNew()

        self.logger.info("**** Providing Customer Info")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Vendors")
        self.addcust.setVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Vicky")
        self.addcust.setLastName("Bora")
        self.addcust.setDOB("03/04/1987")
        self.addcust.setCompName("QA")
        self.addcust.setAdminContent("This IS For Testing")
        self.addcust.clickOnSave()
        time.sleep(5)

        self.logger.info("**** Saving Customer Info")

        self.logger.info("**** Add Customer Validation Started ****")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*** Add Customer Test Passed")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\vkbora\\PycharmProjects\\nopcommerceApp\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("**** Add Customer Test Failed")
            assert True == False

        self.driver.close()
        self.logger.info("**** Ending Home Page Title Test ***")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
