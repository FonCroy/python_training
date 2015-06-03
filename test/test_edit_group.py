# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_by_index(app):
    app.group.edit_group_by_index(Group(name='Group name 1', header='Group header 1', footer='Group footer 1'), 0)
