# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name="GroupName", header="GroupHeader", footer="GroupFooter"))
    old_groups = app.group.get_group_list()
    group = Group(name='Group name 1', header='Group header 1', footer='Group footer 1')
    group.group_id = old_groups[0].group_id
    app.group.edit_group_by_index(group, 0)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
