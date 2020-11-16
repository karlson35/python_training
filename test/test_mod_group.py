__author__ = 'Igor Nikolaev'
from model.group import Group
from random import randrange


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    group = Group(name="group1 modified", header="group header modified", footer="group footer modified")
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    group = Group(name="group name modified2")
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    group = Group(header="group header modified2")
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)