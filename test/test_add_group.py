# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group name 1", header="Group header 1", footer="Group footer 1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
