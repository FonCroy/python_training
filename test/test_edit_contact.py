# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="First", middle_name="Middle", last_name="Last"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(first_name="FirstName", middle_name="MiddleName", last_name="LastName", nickname="NickName",
                          company="Test", mobile_phone="+79805894179", email="example@gmail.com", year_of_birth="2000")
    new_contact.contact_id = contact.contact_id
    app.contact.edit_contact_by_id(new_contact, contact.contact_id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
