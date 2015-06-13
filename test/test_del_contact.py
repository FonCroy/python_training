# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_contact_by_index_from_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="FirstName"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact_by_index_from_home_page(0)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

def test_delete_contact_by_index_from_contact_form(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="FirstName"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact_by_index_from_contact_form(0)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
