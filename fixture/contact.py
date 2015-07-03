# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        """Добавление контакта"""
        wd = self.app.wd
        # init new contact creation
        wd.find_element_by_css_selector("a[href='edit.php']").click()
        # fill new contact information
        self.fill_contact_form(contact)
        # submit new contact
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, input_text):
        wd = self.app.wd
        if input_text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(input_text)

    def change_select_value(self, field_name, input_text):
        wd = self.app.wd
        if input_text is not None:
            select = Select(wd.find_element_by_name(field_name))
            select.select_by_value(input_text)

    def fill_contact_form(self, contact):
        """Заполенение полей на форме контакта"""
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_value('bday', contact.day_of_birth)
        self.change_select_value('bmonth', contact.month_of_birth)
        self.change_field_value("byear", contact.year_of_birth)
        self.change_select_value('aday', contact.day_of_anniversary)
        self.change_select_value('amonth', contact.month_of_anniversary)
        self.change_field_value("ayear", contact.year_of_anniversary)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def delete_contact_by_index_from_home_page(self, index):
        """Удаление сотрудника по порядковому номеру в таблице ( на домашней странице )"""
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id_from_home_page(self, id):
        """Удаление сотрудника по id ( на домашней странице )"""
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_index_from_contact_form(self, index):
        """Удаление сотрудника по порядковому номеру в таблице ( из его карточки )"""
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        self.contact_cache = None

    def delete_contact_by_id_from_contact_form(self, id):
        """Удаление сотрудника по id ( из его карточки )"""
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        """Открыть для редактирования карточку сотрудника по порядковому номеру в таблице"""
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector('a[href^="edit.php?id="]')[index].click()

    def open_contact_to_edit_by_id(self, id):
        """Открыть для редактирования карточку сотрудника по id"""
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector('a[href^="edit.php?id=%s"]' % id).click()

    def open_contact_to_view_by_index(self, index):
        """Открыть для просмотра карточку сотрудника по порядковому номеру в таблице"""
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector('a[href^="view.php?id="]')[index].click()

    def edit_contact_by_index(self, contact, index):
        """Редактирование карточки сотрудника по порядковому номеру в таблице"""
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_css_selector("input[value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, contact, id):
        """Редактирование карточки сотрудника по id"""
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        wd.find_element_by_css_selector("input[value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        """Возвращение количества записей в списке сотрудников"""
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_home_page(self):
        """Возвращение на домашнюю страницу"""
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_css_selector("a[href='./']").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                last_name = element.find_element_by_css_selector("td:nth-child(2)").text
                first_name = element.find_element_by_css_selector("td:nth-child(3)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                all_emails = element.find_element_by_css_selector("td:nth-child(5)").text
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                value = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, contact_id=value,
                                                  address=address, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_details_from_edit_page(self):
        wd = self.app.wd
        contact_id = wd.find_element_by_name("id").get_attribute("value")
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(contact_id=contact_id, last_name=last_name, first_name=first_name, address=address, email=email,
                       email2=email2, email3=email3, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone2=phone2)

    def get_contact_details_from_view_page(self):
        wd = self.app.wd
        all_contact_details = wd.find_element_by_id("content").text
        home_phone = re.search('H: (.*)', all_contact_details).group(1)
        mobile_phone = re.search('M: (.*)', all_contact_details).group(1)
        work_phone = re.search('W: (.*)', all_contact_details).group(1)
        phone2 = re.search('P: (.*)', all_contact_details).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2)
