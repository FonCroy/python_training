# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_contact_by_index_from_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="FirstName"))
    app.contact.delete_contact_by_index_from_home_page(0)


def test_delete_contact_by_index_from_contact_form(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="FirstName"))
    app.contact.delete_contact_by_index_from_contact_form(0)
