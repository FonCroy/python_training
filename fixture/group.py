# -*- coding: utf-8 -*-
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        """Открыть страницу групп"""
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        """Создание группы"""
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        """Возвращение на страницу групп"""
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_group_form(self, group):
        """Заполнение полей на форме группы"""
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.header)

    def delete_group_by_index(self, index):
        """Удаление группы по порядковому номеру в таблице"""
        wd = self.app.wd
        self.open_groups_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_group_by_index(self, group, index):
        """Редактировать группу по порядковому номеру в таблице"""
        wd = self.app.wd
        self.open_groups_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("edit").click()
        # fill group firm
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
