# -*- coding: utf-8 -*-
import re
from random import randrange


def test_all_contacts_fields_from_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    app.contact.open_contact_to_edit_by_index(index)
    contact_from_edit_page = app.contact.get_contact_details_from_edit_page()
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
"""
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    app.contact.open_contact_to_edit_by_index(0)
    contact_from_edit_page = app.contact.get_contact_details_from_edit_page()
    assert contact_from_home_page.all_phones_from_home_page == merge_phones(contact_from_edit_page)


def test_phones_on_contact_details_page(app):
    app.contact.open_contact_to_edit_by_index(0)
    contact_from_edit_page = app.contact.get_contact_details_from_edit_page()
    app.contact.open_contact_to_view_by_index(0)
    contact_from_view_page = app.contact.get_contact_details_from_view_page()
    assert contact_from_edit_page.home_phone == contact_from_view_page.home_phone
    assert contact_from_edit_page.mobile_phone == contact_from_view_page.mobile_phone
    assert contact_from_edit_page.work_phone == contact_from_view_page.work_phone
    assert contact_from_edit_page.phone2 == contact_from_view_page.phone2
"""