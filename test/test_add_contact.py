# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    if contact.group == "random":
        contact.group = random.choice(app.group.get_group_list()).name
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(),
                                                                     key=Contact.id_or_max)
