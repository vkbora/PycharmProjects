from selenium import webdriver
import unittest
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.Pages.loginPage import LoginPage
from POM.Pages.homePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(2)

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # time.sleep(2)
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        # time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vkbora/PycharmProjects/SeleniumWebdriver/reports'))
