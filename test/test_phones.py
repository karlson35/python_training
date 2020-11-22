__author__ = 'Igor Nikolaev'
import re
from random import randrange


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.tel_home == contact_from_edit_page.tel_home
    assert contact_from_view_page.tel_mobile == contact_from_edit_page.tel_mobile
    assert contact_from_view_page.tel_work == contact_from_edit_page.tel_work
    assert contact_from_view_page.tel_fax == contact_from_edit_page.tel_fax
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def test_compare_some_contact_on_home_and_edit_pages(app):
    contacts_from_home_page = app.contact.get_contact_list()
    index = randrange(len(contacts_from_home_page))
    contact_from_home_page = contacts_from_home_page[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_home_page.lastname) == clear(contact_from_edit_page.lastname)
    assert clear(contact_from_home_page.firstname) == clear(contact_from_edit_page.firstname)
    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.tel_home, contact.tel_mobile, contact.tel_work, contact.phone2]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))

