# coding=utf-8
from __future__ import annotations

from .base.base_element import BaseElement


class Label(BaseElement):

    def __init__(self,
                 search_condition: str,
                 locator: str,
                 name: str) -> None:
        super(Label, self).__init__(search_condition_of=search_condition, loc=locator, name_of=name)

    def __getitem__(self, key: str) -> Label:
        new_element = super(Label, self).__getitem__(key=key)
        return Label(new_element.get_search_condition(), new_element.get_locator(), new_element.get_name())

    def __call__(self, sublocator: str, new_name_of: str | None = None) -> Label:
        new_element = super(Label, self).__call__(sublocator=sublocator, new_name_of=new_name_of)
        return Label(new_element.get_search_condition(), new_element.get_locator(), new_element.get_name())
