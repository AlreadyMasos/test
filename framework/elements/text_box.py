# coding=utf-8
from __future__ import annotations
from framework.utils.logger import Logger
from .base.base_element import BaseElement


class TextBox(BaseElement):
    def __init__(self,
                 search_condition: str,
                 locator: str,
                 name: str) -> None:
        super(TextBox, self).__init__(search_condition_of=search_condition, loc=locator, name_of=name)

    def __getitem__(self, key: str) -> TextBox:
        new_element = super(TextBox, self).__getitem__(key=key)
        return TextBox(new_element.get_search_condition(), new_element.get_locator(), new_element.get_name())

    def __call__(self, sublocator: str, new_name_of: str | None = None) -> TextBox:
        new_element = super(TextBox, self).__call__(sublocator=sublocator, new_name_of=new_name_of)
        return TextBox(new_element.get_search_condition(), new_element.get_locator(), new_element.get_name())

    def send_text(self, word):
        Logger.info(f"{self.get_name()}: установленый текст {word}")
        self.find_element().send_keys(word)
