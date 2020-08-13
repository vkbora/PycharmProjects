class SearchCustomer:
    # Add customer page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//*[@id='customers-grid']"
    tableRows_xpath = "//*[@id='customers-grid']/tbody/tr"
    tableColumns_xpath = "//*[@id='customers-grid'/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        emails = self.driver.find_element_by_id(self.txtEmail_id)
        emails.clear()
        emails.send_keys(email)

    def setFirstName(self, fname):
        firstname = self.driver.find_element_by_id(self.txtFirstName_id)
        firstname.clear()
        firstname.send_keys(fname)

    def setLastName(self, lname):
        lastname = self.driver.find_element_by_id(self.txtLastName_id)
        lastname.clear()
        lastname.send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        print(len(self.driver.find_elements_by_xpath(self.tableRows_xpath)))
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        print(len(self.driver.find_elements_by_xpath(self.tableColumns_xpath)))
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailId = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailId == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            nameId = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if nameId == name:
                flag = True
                break
        return flag
