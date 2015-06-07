# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name="GroupName", header="GroupHeader", footer="GroupFooter"))
    app.group.edit_group_by_index(Group(name='Group name 1', header='Group header 1', footer='Group footer 1'), 0)
