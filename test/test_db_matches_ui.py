__author__ = 'Igor Nikolaev'

from model.contact import Contact
from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = list(map(clean, db.get_group_list()))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()

    def clean(contact):
        return Contact(id=contact.id, firstname=" ".join(contact.firstname.strip().split()),
                       lastname=" ".join(contact.lastname.strip().split()),
                       middlename=" ".join(contact.middlename.strip().split()),
                       nickname=" ".join(contact.nickname.strip().split()),
                       address=" ".join(contact.address.strip().split()))
    db_list = list(map(clean, db.get_contact_list()))
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)