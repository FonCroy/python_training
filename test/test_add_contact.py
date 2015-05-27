# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="First", middle_name="Middle", last_name="Last", nickname="FML",
                               company="Test Inc.", mobile_phone="+79205894179", email="test@gmail.com",
                               year_of_birth="1978"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", middle_name="", last_name="", nickname="", company="", mobile_phone="",
                               email="", year_of_birth=""))
    app.session.logout()
