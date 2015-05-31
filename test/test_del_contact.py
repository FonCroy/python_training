# -*- coding: utf-8 -*-
def test_delete_contact_by_index_from_home_page(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact_by_index_from_home_page(0)
    app.session.logout()

def test_delete_contact_by_index_from_contact_form(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact_by_index_from_contact_form(0)
    app.session.logout()