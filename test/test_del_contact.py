__author__ = 'Igor Nikolaev'
import random
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_empty()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert sorted(old_contacts) == sorted(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(),
                                                                     key=Contact.id_or_max)

