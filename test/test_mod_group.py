__author__ = 'Igor Nikolaev'
from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = Group(name="group1 modified", header="group header modified", footer="group footer modified")
    old_groups = db.get_group_list()
    group_to_mod = random.choice(old_groups)
    app.group.modify_group_by_id(group, group_to_mod.id)
    for tmp_group in old_groups:
        if tmp_group.id == group_to_mod.id:
            tmp_group.name = group.name
            tmp_group.header = group.header
            tmp_group.footer = group.footer
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


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