# -*- coding: utf-8 -*-
def test_delete_contact_by_index_from_home_page(app):
    app.contact.delete_contact_by_index_from_home_page(1)


def test_delete_contact_by_index_from_contact_form(app):
    app.contact.delete_contact_by_index_from_contact_form(1)
