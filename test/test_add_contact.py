# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import calendar


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_tel(maxlen):
    symbols = string.digits + "()- "
    return "".join([random.choice(symbols) for i in range(maxlen)])


# def test_random_group_name(app):
#    s = app.group.get_group_list()
#    s2 = []
#    for i in range(len(s)):
#        s2.append(s[i].name)
#    return random.choice(s2)


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    tel_home="", tel_mobile="", tel_work="", tel_fax="", email1="", email2="", email3="", homepage="",
                    bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", group="[none]", address2="",
                    phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                       title=random_string("title", 10), company=random_string("company", 10),
                       address=random_string("address", 10), tel_home=random_tel(10),
                       tel_mobile=random_tel(10), tel_work=random_tel(10), tel_fax=random_tel(10),
                       email1=random_string("email1", 10), email2=random_string("email2", 10),
                       email3=random_string("email3", 10), homepage=random_string("homepage", 10),
                       bday=str(random.randrange(31)), bmonth=random.choice(calendar.month_name[1:13]),
                       byear=random.randrange(1900, 2020), aday=str(random.randrange(31)),
                       amonth=random.choice(calendar.month_name[1:13]), ayear=random.randrange(1900, 2050),
                       group="[none]", address2=random_string("address2", 10), phone2=random_tel(10),
                       notes=random_string("notes", 10))
               for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
