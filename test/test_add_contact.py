# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Igor", middlename="Nikolaev", lastname="sdasd", nickname="asdasdasfasd",
                       title="title", company="company", address="address",
                       tel_home="tel_home", tel_mobile="tel_mobile", tel_work="tel_work", tel_fax="tel_fax",
                       email1="email1", email2="email2", email3="email3", homepage="homepage",
                       bday="12", bmonth="August", byear="1983", aday="14", amonth="October", ayear="2004",
                       group="[none]", address2="secondary_address", phone2="secondary_phone",
                       notes="notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_empty()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(Contact())
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)