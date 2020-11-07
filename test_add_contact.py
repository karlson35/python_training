# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Igor")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Nikolaev")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("sdasd")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("asdasdasfasd")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("address")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("telhome")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("tel_mobile")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("tel_work")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("tel_fax")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email1")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("email2")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("imail3")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("homepage")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("6")
        wd.find_element_by_xpath("//option[@value='6']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_xpath("//option[@value='June']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1985")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("9")
        wd.find_element_by_xpath("(//option[@value='9'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("July")
        wd.find_element_by_xpath("(//option[@value='July'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2005")
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("group1")
        wd.find_element_by_xpath("(//option[@value='2'])[3]").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("seconadary_address")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("secondary_home")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("notes")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
