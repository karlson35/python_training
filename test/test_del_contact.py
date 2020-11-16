__author__ = 'Igor Nikolaev'


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_empty()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

