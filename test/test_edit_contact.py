# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_by_index(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact_by_index(Contact(first_name="FirstName", middle_name="MiddleName", last_name="LastName",
                                              nickname="NickName", company="Test", mobile_phone="+79805894179",
                                              email="example@gmail.com", year_of_birth="2000"), 0)
    app.session.logout()
