__author__ = 'Igor Nikolaev'
from model.contact import Contact
import random


def test_modify_some_contact(app, db):
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
            tmp_contact.firstname = contact_to_mod.contact_to_mod.firstname
            tmp_contact.middlename = contact_to_mod.middlename
            tmp_contact.lastname = contact_to_mod.lastname
            tmp_contact.nickname = contact_to_mod.nickname
            tmp_contact.title = contact_to_mod.title
            tmp_contact.company = contact_to_mod.company
            tmp_contact.address = contact_to_mod.address
            tmp_contact.tel_home = contact_to_mod.tel_home
            tmp_contact.tel_mobile = contact_to_mod.tel_mobile
            tmp_contact.tel_work = contact_to_mod.tel_work
            tmp_contact.tel_fax = contact_to_mod.tel_fax
            tmp_contact.email1 = contact_to_mod.email1
            tmp_contact.email2 = contact_to_mod.email2
            tmp_contact.email3 = contact_to_mod.email3
            tmp_contact.homepage = contact_to_mod.homepage
            tmp_contact.bday = contact_to_mod.bday
            tmp_contact.bmonth = contact_to_mod.bmonth
            tmp_contact.byear = contact_to_mod.byear
            tmp_contact.aday = contact_to_mod.aday
            tmp_contact.amonth = contact_to_mod.amonth
            tmp_contact.ayear = contact_to_mod.ayear
            tmp_contact.group = contact_to_mod.group
            tmp_contact.address2 = contact_to_mod.address2
            tmp_contact.phone2 = contact_to_mod.phone2
            tmp_contact.notes = contact_to_mod.notes
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
