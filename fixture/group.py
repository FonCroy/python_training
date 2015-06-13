# -*- coding: utf-8 -*-
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        """Открыть страницу групп"""
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_css_selector("a[href='group.php']").click()

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
        self.group_cache = None

    def return_to_groups_page(self):
        """Возвращение на страницу групп"""
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_css_selector("a[href='group.php']").click()

    def change_field_value(self, field_name, input_text):
        """Изменить значение поля"""
        wd = self.app.wd
        if input_text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(input_text)

    def fill_group_form(self, group):
        """Заполнение полей на форме группы"""
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def delete_group_by_index(self, index):
        """Удаление группы по порядковому номеру в таблице"""
        wd = self.app.wd
        self.open_groups_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        """Возвращение количества записей в списке групп"""
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

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
        self.group_cache = None

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                value = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, group_id=value))
        return list(self.group_cache)
