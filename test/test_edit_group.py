# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="GroupName", header="GroupHeader", footer="GroupFooter"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name='Group name 1', header='Group header 1', footer='Group footer 1')
    new_group.group_id = group.group_id
    app.group.edit_group_by_id(new_group, group.group_id)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
