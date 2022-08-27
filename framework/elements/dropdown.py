# coding=utf-8
from .base.base_element import BaseElement


class Dropdown(BaseElement):

    def __init__(self, search_condition, locator, name):
        super(Dropdown, self).__init__(search_condition_of=search_condition, loc=locator, name_of=name)

    def __getitem__(self, key):
        new_element = super(Dropdown, self).__getitem__(key=key)
        return Dropdown(new_element.get_search_condition(), new_element.get_locator(), new_element.get_name())

    def __call__(self, sublocator, new_name_of=None):
        new_element = super(Dropdown, self).__call__(sublocator=sublocator, new_name_of=new_name_of)
        return Dropdown(new_element.get_search_condition(), new_element.get_locator(), new_element.get_name())

    def get_element_type(self):
        return "Dropdown"
