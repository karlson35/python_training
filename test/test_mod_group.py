__author__ = 'Igor Nikolaev'
from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group((Group(name="group1 modified", header="group header modified", footer="group footer "
                                                                                                       "modified")))
    app.session.logout()
