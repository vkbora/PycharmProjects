import time

import pytest

from pageObjects.loginPage import LoginPage
from untilities.readProperties import ReadConfig
from untilities.customLogger import LogGen
from untilities import XLUtils


class Test_002_Login_ddt:
    baseURL = ReadConfig.getAppURL()
    path = "C:/Users/vkbora/PycharmProjects/nopcommerceApp/TestData/Test_DDT.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************** Test_002_Login_ddt ************")
        self.logger.info("*** Verifying Login Test ***")

        self.driver = setup
        # self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.gerRowCount(self.path, 'Sheet1')
        print("Number of rows : " + str(self.rows))

        listStatus = []  # Empty List variable

        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.status = XLUtils.readData(self.path, 'Sheet1', r, 3)
            XLUtils.writeData(self.path, 'Sheet1', r, 4, "Ok")

            self.driver.get(self.baseURL)
            time.sleep(2)
            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.status == "Pass":
                    self.logger.info("****** Passes ******")
                    self.lp.clickLogout()
                    listStatus.append("Pass")

                elif self.status == "Fail":
                    self.logger.info("***** Failed ****")
                    self.lp.clickLogout()
                    listStatus.append("Fail")

            elif act_title != exp_title:
                if self.status == "Pass":
                    self.logger.info("***** Failed *****")
                    listStatus.append("Fail")

                elif self.status == "Fail":
                    self.logger.info("*********** Passed ******")
                    listStatus.append("Pass")

        if "Fail" not in listStatus:
            self.logger.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("End Of Login DDT Test")
        self.logger.info("Completed TC_LoginDDT_002")
