# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Igor", middlename="Nikolaev", lastname="sdasd", nickname="asdasdasfasd",
                       title="title", company="company", address="address",
                       tel_home="tel_home", tel_mobile="tel_mobile", tel_work="tel_work", tel_fax="tel_fax",
                       email1="email1", email2="email2", email3="email3", homepage="homepage",
                       bday="12", bmonth="August", byear="1983", aday="14", amonth="October", ayear="2004",
                       group="[none]", address2="secondary_address", phone2="secondary_phone",
                       notes="notes"))


def test_add_empty_contact(app):
    app.contact.create_empty()