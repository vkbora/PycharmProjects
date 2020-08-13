import unittest
import HtmlTestRunner
from selenium import webdriver


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_name(self):
        self.driver.get("https://www.google.co.in/")
        self.driver.find_element_by_name("q").send_keys("vickkkkkkkkkkkkkkkkkk")
        self.driver.find_element_by_name("btnK").click()

    def test_search_surname(self):
        self.driver.get("https://www.google.co.in/")
        self.driver.find_element_by_name("q").send_keys("vireeeeeeeeeeeeeeeeee")
        self.driver.find_element_by_class_name("gNO89b").click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vkbora/PycharmProjects/SeleniumWebdriver/reports'))
