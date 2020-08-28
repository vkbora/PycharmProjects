from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(
            executable_path="C:/Users/vkbora/PycharmProjects/SeleniumWebdriver/drivers/chromedriver.exe")
        print("### Chrome Browser ###")
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path="C:/Users/vkbora/PycharmProjects/SeleniumWebdriver/drivers/geckodriver.exe")
        print("### Firefox Browser ###")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will the Browser value to setup method
    return request.config.getoption("--browser")
