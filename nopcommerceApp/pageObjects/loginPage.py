class LoginPage:
    txt_username_id = "Email"
    txt_password_id = "Password"
    button_Login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    link_logout_xpath = "/html/body/div[3]/div[1]/div/div/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.txt_username_id).clear()
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.txt_password_id).clear()
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_Login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()