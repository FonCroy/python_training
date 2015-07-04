# -*- coding: utf-8 -*-
import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, name, header, footer) = row
                list.append(Group(group_id=str(group_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3\
            from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (contact_id, first_name, last_name, address, home_phone, mobile_phone, work_phone, phone2, email,
                 email2, email3) = row
                list.append(Contact(contact_id=str(contact_id), first_name=first_name, last_name=last_name,
                                    address=address, home_phone=home_phone, mobile_phone=mobile_phone,
                                    work_phone=work_phone, phone2=phone2, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
