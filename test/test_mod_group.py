__author__ = 'Igor Nikolaev'
from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="group1 modified", header="group header modified", footer="group footer "
                                                                                                       "modified"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="group name modified2"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="group header modified2"))