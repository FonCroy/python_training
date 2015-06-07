# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="First", middle_name="Middle", last_name="Last"))
    app.contact.edit_contact_by_index(Contact(first_name="FirstName", middle_name="MiddleName", last_name="LastName",
                                              nickname="NickName", company="Test", mobile_phone="+79805894179",
                                              email="example@gmail.com", year_of_birth="2000"), 0)
