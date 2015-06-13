# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="First", middle_name="Middle", last_name="Last"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="FirstName", middle_name="MiddleName", last_name="LastName", nickname="NickName",
                      company="Test", mobile_phone="+79805894179", email="example@gmail.com", year_of_birth="2000")
    contact.contact_id = old_contacts[0].contact_id
    app.contact.edit_contact_by_index(contact, 0)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

