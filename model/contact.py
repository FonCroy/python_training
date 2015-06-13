# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, company=None,
                 mobile_phone=None, email=None, year_of_birth=None, contact_id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.company = company
        self.mobile_phone = mobile_phone
        self.email = email
        self.year_of_birth = year_of_birth
        self.contact_id = contact_id

    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.first_name, self.last_name)

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and \
            (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
