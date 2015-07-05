# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_delete_some_contact_from_home_page(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="FirstName"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id_from_home_page(contact.contact_id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

def test_delete_some_contact_from_contact_form(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="FirstName"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id_from_contact_form(contact.contact_id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

def test_delete_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="TestName", header="TestHeader", footer="TestFooter"))
    group_list = orm.get_group_list()
    random_group = random.choice(group_list)
    if len(orm.get_contact_list()) == 0:
        app.contact.add_new(Contact(first_name="FirstName"))
    if len(orm.get_contacts_in_group(random_group)) == 0:
        contact = random.choice(orm.get_contacts_not_in_group(random_group))
        app.contact.add_contact_to_group(contact, random_group)
    contact = random.choice(orm.get_contacts_in_group(random_group))
    old_contacts_in_target_group = orm.get_contacts_in_group(random_group)
    app.contact.delete_contact_from_group(contact, random_group)
    new_contacts_in_target_group = orm.get_contacts_in_group(random_group)
    old_contacts_in_target_group.remove(contact)
    assert sorted(old_contacts_in_target_group, key=Contact.id_or_max) == sorted(new_contacts_in_target_group,
                                                                                 key=Contact.id_or_max)
