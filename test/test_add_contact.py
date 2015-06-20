# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contact import Contact


def random_string(prefix, max_len):
    symbol = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(max_len))])


def random_phone(max_len):
    return "+" + random.choice(string.digits) + " " \
           + "".join([random.choice(string.digits) for i in range(max_len)]).rstrip()


def random_digits(max_len):
    return str(random.randrange(max_len))


def random_day():
    return random.randint(1, 31)


def random_month():
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]
    return month[random.randrange(len(month))]


def random_email(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return (prefix + '_' + "".join([random.choice(symbols) for i in range(random.randrange(max_len))]) + '@'
            + "".join([random.choice(symbols) for i in range(random.randrange(max_len))]) + '.com')

test_data = [Contact(first_name="", middle_name="", last_name="")] + \
            [Contact(first_name=random_string("firstname", 20), middle_name=random_string("middlename", 20),
                     last_name=random_string("lastname", 20), nickname=random_string("nickname", 15),
                     title=random_string("title", 20), company=random_string("company", 20),
                     address=random_string("address", 25), homepage=random_string("homepage", 25),
                     home_phone=random_phone(9), mobile_phone=random_phone(9), work_phone=random_phone(9),
                     fax=random_phone(9), phone2=random_phone(9), email=random_email('email', 10),
                     email2=random_email('email2', 10), email3=random_email('email3', 10),
                     day_of_birth=random_digits(31), month_of_birth=random_month(), year_of_birth=random_digits(9999),
                     notes=random_string("notes", 25), day_of_anniversary=random_digits(31),
                     month_of_anniversary=random_month(), year_of_anniversary=random_digits(9999),
                     address2=random_string("address_secondary", 25))
             for i in range(5)
             ]


@pytest.mark.parametrize("contact", test_data, ids=[repr(i) for i in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)