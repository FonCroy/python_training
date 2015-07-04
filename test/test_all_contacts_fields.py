# -*- coding: utf-8 -*-
import re
from model.contact import Contact


def test_all_contacts_fields_from_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(map(clear_contacts_from_db, db.get_contact_list()), key=Contact.id_or_max)
    assert contacts_from_home_page == contacts_from_db

def clear_contacts_from_db(contact):
    contact_id = str(contact.contact_id)
    first_name = re.sub(r' {2,}', ' ', contact.first_name).strip()
    last_name = re.sub(r' {2,}', ' ', contact.last_name).strip()
    address = re.sub(r'\r', '', re.sub(r' {2,}', ' ', contact.address)).strip()
    all_phones = merge_phones(contact)
    all_emails = merge_emails(contact)
    return Contact(contact_id=contact_id, first_name=first_name, last_name=last_name, address=address,
                   all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails)

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.phone2]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
