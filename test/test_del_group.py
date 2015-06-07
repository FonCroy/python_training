# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name="GroupName"))
    app.group.delete_group_by_index(0)
