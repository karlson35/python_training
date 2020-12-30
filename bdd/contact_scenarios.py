__author__ = 'Igor Nikolaev'

from pytest_bdd import scenario
from .contact_steps import *


@scenario('contacts.feature', 'Add new contact')
def test_add_contact():
    pass


@scenario('contacts.feature', 'Delete contact')
def test_del_contact():
    pass


@scenario('contacts.feature', 'Modify contact')
def test_mod_contact():
    pass
