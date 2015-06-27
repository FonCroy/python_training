# -*- coding: utf-8 -*-
import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
output_file = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        output_file = a

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
                     address2=random_string("address2", 25))
             for i in range(5)
             ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_file)
with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(test_data))
