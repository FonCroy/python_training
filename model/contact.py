# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None, email=None, email2=None,
                 email3=None, homepage=None, year_of_birth=None, day_of_birth=None, month_of_birth=None, address2=None,
                 year_of_anniversary=None, day_of_anniversary=None, month_of_anniversary=None, phone2=None, notes=None,
                 contact_id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.year_of_birth = year_of_birth
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_anniversary = year_of_anniversary
        self.day_of_anniversary = day_of_anniversary
        self.month_of_anniversary = month_of_anniversary
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.contact_id = contact_id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) \
               and ' '.join(self.first_name.split()) == ' '.join(other.first_name.split()) \
               and ' '.join(self.last_name.split()) == ' '.join(other.last_name.split())

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
