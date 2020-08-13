import time
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/a/span"
    lnkCustomers_submenu_xpath = "//span[@class='menu-item-title'][contains(text(), 'Customers')]"
    btnAddNew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    ck_maleGender_id = "Gender_Male"
    ck_femaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    listAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    listGuests_xpath = "//li[contains(text(), 'Guests')]"
    listVendors_xpath = "//li[contains(text(), 'Vendors')]"
    dd_vendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerSubMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_submenu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        if role == "Administrators":
            self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
            time.sleep(2)
            self.lstitem = self.driver.find_element_by_xpath(self.listAdministrators_xpath)

        elif role == "Vendors":
            self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
            time.sleep(2)
            self.lstitem = self.driver.find_element_by_xpath(self.listVendors_xpath)

        else:
            # role == "Guests"
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div/form/div[3]/div/nop-panels/nop-panel/div/div[2]/div[1]/div[10]/div["
                "2]/div/div[1]/div/ul/li/span[2]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
            time.sleep(2)
            self.lstitem = self.driver.find_element_by_xpath(self.listGuests_xpath)

        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.lstitem)

    def setVendor(self, value):
        dropdown = Select(self.driver.find_element_by_xpath(self.dd_vendor_xpath))
        dropdown.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.ck_maleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.ck_femaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.ck_maleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDOB(self, dob):
        self.driver.find_element_by_xpath(self.txtDOB_xpath).send_keys(dob)

    def setCompName(self, compName):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(compName)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
