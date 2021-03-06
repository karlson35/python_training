__author__ = 'Igor Nikolaev'

from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_empty(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_information(self, contact):
        wd = self.app.wd
        if contact.firstname is not None:
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename is not None:
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
        if contact.lastname is not None:
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname is not None:
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.title is not None:
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)
        if contact.company is not None:
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company)
        if contact.address is not None:
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.tel_home is not None:
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.tel_home)
        if contact.tel_mobile is not None:
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.tel_mobile)
        if contact.tel_work is not None:
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.tel_work)
        if contact.tel_fax is not None:
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contact.tel_fax)
        if contact.email1 is not None:
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email1)
        if contact.email2 is not None:
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3 is not None:
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.homepage is not None:
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if contact.bday is not None:
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        if contact.bmonth is not None:
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        if contact.byear is not None:
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.byear)
        if contact.aday is not None:
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        if contact.amonth is not None:
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        if contact.ayear is not None:
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contact.ayear)
        if self.check_exists_by_name("new_group"):
            if contact.group is not None:
                Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group)
        if contact.address2 is not None:
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(contact.address2)
        if contact.phone2 is not None:
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.phone2)
        if contact.notes is not None:
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(contact.notes)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_information(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(contact, 0)

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_information(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_information(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = text[5].text
                all_email = text[4].text
                self.contact_cache.append(Contact(firstname=text[2].text, lastname=text[1].text, address=text[3].text,
                                                  id=id, all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def check_exists_by_name(self, name):
        wd = self.app.wd
        return len(wd.find_elements_by_name(name)) > 0

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        tel_home = wd.find_element_by_name("home").get_attribute("value")
        tel_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        tel_work = wd.find_element_by_name("work").get_attribute("value")
        tel_fax = wd.find_element_by_name("fax").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, tel_home=tel_home, tel_work=tel_work,
                       tel_mobile=tel_mobile, tel_fax=tel_fax, phone2=phone2, email1=email1, email2=email2,
                       email3=email3, id=id)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        tel_home = re.search("H: (.*)", text).group(1)
        tel_mobile = re.search("M: (.*)", text).group(1)
        tel_work = re.search("W: (.*)", text).group(1)
        tel_fax = re.search("F: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(tel_home=tel_home, tel_work=tel_work,
                       tel_mobile=tel_mobile, phone2=phone2, tel_fax=tel_fax)

    def add_to_group(self, contact, group):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % contact.id).click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group.name)
        wd.find_element_by_name("add").click()
        self.return_to_home_page()

    def delete_from_group(self, contact, group):
        wd = self.app.wd
        self.return_to_home_page()
        Select(wd.find_element_by_name("group")).select_by_visible_text(group.name)
        wd.find_element_by_css_selector("input[value='%s']" % contact.id).click()
        wd.find_element_by_name("remove").click()
        self.return_to_home_page()
        Select(wd.find_element_by_name("group")).select_by_visible_text('[all]')