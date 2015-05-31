# -*- coding: utf-8 -*-
def test_delete_group_by_index(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_group_by_index(0)
    app.session.logout()
