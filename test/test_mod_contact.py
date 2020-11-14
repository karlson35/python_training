__author__ = 'Igor Nikolaev'
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_empty()
    contact = Contact(firstname="Vasya", middlename="Pupkin", lastname="sdasd", nickname="vasyan007",
                       title="title", company="company", address="address",
                       tel_home="tel_home", tel_mobile="tel_mobile", tel_work="tel_work", tel_fax="tel_fax",
                       email1="email1", email2="email2", email3="email3", homepage="homepage",
                       bday="12", bmonth="August", byear="1983", aday="14", amonth="October", ayear="2004",
                       group="[none]", address2="secondary_address", phone2="secondary_phone",
                       notes="notes")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
