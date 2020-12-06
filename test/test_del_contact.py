__author__ = 'Igor Nikolaev'
import random
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_empty()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=" ".join(contact.firstname.strip().split()),
                           lastname=" ".join(contact.lastname.strip().split()),
                           middlename=" ".join(contact.middlename.strip().split()),
                           nickname=" ".join(contact.nickname.strip().split()),
                           address=" ".join(contact.address.strip().split()))

        db_list = list(map(clean, db.get_contact_list()))
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
