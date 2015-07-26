# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random
import pytest


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('When I add the contact %s to the list' % contact):
        app.contact.create(contact)
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        with pytest.allure.step('Also check UI'):
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="TestName", header="TestHeader", footer="TestFooter"))
    group_list = orm.get_group_list()
    random_group = random.choice(group_list)
    if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_not_in_group(random_group)) == 0:
        app.contact.create(Contact(first_name="FirstName"))
    random_contact = random.choice(orm.get_contacts_not_in_group(random_group))
    old_contacts_in_random_group = orm.get_contacts_in_group(random_group)
    app.contact.add_contact_to_group(random_contact, random_group)
    new_contacts_in_random_group = orm.get_contacts_in_group(random_group)
    old_contacts_in_random_group.append(random_contact)
    assert sorted(old_contacts_in_random_group, key=Contact.id_or_max) == sorted(new_contacts_in_random_group,
                                                                                 key=Contact.id_or_max)
