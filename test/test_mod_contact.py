__author__ = 'Igor Nikolaev'
from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_empty()
    contact = Contact(firstname="Vasya", middlename="Pupkin", lastname="sdasd", nickname="vasyan007",
                       title="title", company="company", address="address",
                       tel_home="tel_home", tel_mobile="tel_mobile", tel_work="tel_work", tel_fax="tel_fax",
                       email1="email1", email2="email2", email3="email3", homepage="homepage",
                       bday="12", bmonth="August", byear="1983", aday="14", amonth="October", ayear="2004",
                       group="[none]", address2="secondary_address", phone2="secondary_phone",
                       notes="notes")
    old_contacts = db.get_contact_list()
    contact_to_mod = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact, contact_to_mod.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for tmp_contact in old_contacts:
        if tmp_contact.id == contact_to_mod.id:
            tmp_contact.firstname = contact.firstname
            tmp_contact.middlename = contact.middlename
            tmp_contact.lastname = contact.lastname
            tmp_contact.nickname = contact.nickname
            tmp_contact.title = contact.title
            tmp_contact.company = contact.company
            tmp_contact.address = contact.address
            tmp_contact.tel_home = contact.tel_home
            tmp_contact.tel_mobile = contact.tel_mobile
            tmp_contact.tel_work = contact.tel_work
            tmp_contact.tel_fax = contact.tel_fax
            tmp_contact.email1 = contact.email1
            tmp_contact.email2 = contact.email2
            tmp_contact.email3 = contact.email3
            tmp_contact.homepage = contact.homepage
            tmp_contact.bday = contact.bday
            tmp_contact.bmonth = contact.bmonth
            tmp_contact.byear = contact.byear
            tmp_contact.aday = contact.aday
            tmp_contact.amonth = contact.amonth
            tmp_contact.ayear = contact.ayear
            tmp_contact.group = contact.group
            tmp_contact.address2 = contact.address2
            tmp_contact.phone2 = contact.phone2
            tmp_contact.notes = contact.notes
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(),
                                                                     key=Contact.id_or_max)
