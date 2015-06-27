# -*- coding: utf-8 -*-
from model.contact import Contact

test_data = [
    Contact(first_name="", middle_name="", last_name=""),
    Contact(first_name="first_name", middle_name="middle_name", last_name="last_name", nickname="nickname",
            title="title", company="company", address="address", homepage="homepage", home_phone='987-654-321',
            mobile_phone='+79205976249', work_phone='18856-451-458', fax='154845194', phone2='123456789',
            email='email@email.com', email2='email2@email.com', email3='email3@email.com', day_of_birth='12',
            month_of_birth='March', year_of_birth='1980', notes="notes", day_of_anniversary='23',
            month_of_anniversary='August', year_of_anniversary='2005', address2="address2")
    ]
