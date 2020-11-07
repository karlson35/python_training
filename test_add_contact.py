# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.login(wd)
        self.create_contact(wd)
        self.open_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def open_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, firstname="Igor2", middlename="Nikolaev2", lastname="sdasd",
                       nickname="asdasdasfasd", title="title", company="company", address="address", tel_home="tel_home",
                       tel_mobile="tel_mobile", tel_work="tel_work", tel_fax="tel_fax", email1="email1",
                       email2="email2", email3="email3", homepage="homepage", bday="8", bmonth="June", byear="1985",
                       aday="9", amonth="July", ayear="2005", group="[none]", address2="seconadary_address",
                       phone2="secondary_phone", notes="notes"):
        # create contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)

        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)

        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)

        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)

        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)

        wd.find_element_by_name("theform").click()

        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)

        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)

        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(tel_home)

        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(tel_mobile)

        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(tel_work)

        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(tel_fax)

        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email1)

        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)

        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)

        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)

        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(bday)
        wd.find_element_by_xpath("//option[@value="+bday+"]").click()

        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(bmonth)
        wd.find_element_by_xpath("//option[@value='"+bmonth+"']").click()

        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(byear)

        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(aday)
        wd.find_element_by_xpath("(//option[@value="+aday+"])[2]").click()

        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(amonth)
        wd.find_element_by_xpath("(//option[@value='"+amonth+"'])[2]").click()

        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(ayear)

        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(group)
        #разобраться с этим
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        #wd.find_element_by_xpath("(//option[.='group2']").click()

        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)

        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone2)

        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd):
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()

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
