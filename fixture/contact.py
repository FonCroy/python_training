# -*- coding: utf-8 -*-
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        """Добавление контакта"""
        wd = self.app.wd
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill new contact information
        self.fill_contact_form(contact)
        # submit new contact
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        """Заполенение полей на форме контакта"""
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.year_of_birth)

    def delete_contact_by_index_from_home_page(self, index):
        """Удаление сотрудника по порядковому номеру в таблице ( на домашней странице )"""
        wd = self.app.wd
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
        wd.find_elements_by_css_selector('a[href^="edit.php?id="]')[index].click()

    def edit_contact_by_index(self, contact, index):
        """Редактирование карточки сотрудника по порядковому номеру в таблице"""
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_css_selector("input[value='Update']").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        """Возвращение на домашнюю страницу"""
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
