# -*- coding: utf-8 -*-
from model.contact import Contact


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

    def change_fill_value(self, field_name, input_text):
        wd = self.app.wd
        if input_text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(input_text)

    def fill_contact_form(self, contact):
        """Заполенение полей на форме контакта"""
        self.change_fill_value("firstname", contact.first_name)
        self.change_fill_value("middlename", contact.middle_name)
        self.change_fill_value("lastname", contact.last_name)
        self.change_fill_value("nickname", contact.nickname)
        self.change_fill_value("company", contact.company)
        self.change_fill_value("mobile", contact.mobile_phone)
        self.change_fill_value("email", contact.email)
        self.change_fill_value("byear", contact.year_of_birth)

    def delete_contact_by_index_from_home_page(self, index):
        """Удаление сотрудника по порядковому номеру в таблице ( на домашней странице )"""
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()

    def delete_contact_by_index_from_contact_form(self, index):
        """Удаление сотрудника по порядковому номеру в таблице ( из его карточки )"""
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        wd.find_element_by_css_selector("input[value='Delete']").click()

    def open_contact_to_edit_by_index(self, index):
        """Открыть для редактирования карточку сотрудника по порядковому номеру в таблице"""
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector('a[href^="edit.php?id="]')[index].click()

    def edit_contact_by_index(self, contact, index):
        """Редактирование карточки сотрудника по порядковому номеру в таблице"""
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_css_selector("input[value='Update']").click()
        self.return_to_home_page()

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

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            last_name = element.find_element_by_css_selector("td:nth-child(2)").text
            first_name = element.find_element_by_css_selector("td:nth-child(3)").text
            value = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(first_name=first_name, last_name=last_name, contact_id=value))
        return contacts
