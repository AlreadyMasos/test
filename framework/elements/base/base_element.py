# coding=utf-8

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.config.waits import Waits


class BaseElement(object):

    def __init__(self, search_condition_of, loc, name_of):
        self.__search_condition = search_condition_of
        self.__locator = loc
        self.__name = name_of

    def __getitem__(self, key):
        if self.__search_condition != By.XPATH:
            raise TypeError("__getitem__ for BaseElement possible only when __search_condition == By.XPATH")
        else:
            return type(self)(By.XPATH, self.__locator + "[" + str(key) + "]", self.__name)
            # return type(self)(By.XPATH, "(" + self.__locator + ")" + "[" + str(key) + "]", self.__name)

    def __call__(self, sublocator, new_name_of=None):
        if new_name_of is not None:
            return type(self)(By.XPATH, self.__locator + sublocator, new_name_of)
        else:
            return type(self)(By.XPATH, self.__locator + sublocator, self.__name)

    def get_locator(self):
        return self.__locator

    def get_search_condition(self):
        return self.__search_condition

    def get_name(self):
        return self.__name

    def find_element(self):
        waiter = ec.presence_of_element_located((self.get_search_condition(), self.get_locator()))
        element = self.wait_for_check_by_condition(method_to_check=waiter, message=" не был найден")
        return element

    def click(self):
        Logger.info("click: Щелчок по элемету '" + self.get_name() + " " + self.__class__.__name__ + "'")

        def func():
            self.find_element().click()
            return True

        self.wait_for(func)

    @staticmethod
    def wait_for(condition, *args, **kwargs):
        def func(driver):
            try:
                value = condition(*args, **kwargs)
                return value
            except StaleElementReferenceException:
                return False

        return WebDriverWait(Browser.get_browser().get_driver(), Waits.EXPLICITLY_WAIT_SEC,
                             ignored_exceptions=[StaleElementReferenceException]).until(func)

    def send_keys_to_element(self, keys):
        actions = ActionChains(Browser.get_browser().get_driver())
        actions.send_keys_to_element(self.find_element(), keys)
        actions.perform()

    def get_text(self):
        Logger.info("get_text: Получение текста для элемента '" + self.get_name() + "'")
        self.wait_for_is_present()
        text = self.find_element().text
        Logger.info("get_text: Получен текст '" + text + "'")
        return text

    def get_text_content(self):
        self.wait_for_is_visible()
        return Browser.get_browser().get_driver(). \
            execute_script("return arguments[0].textContent;", self.find_element())

    def wait_for_clickable(self):
        waiter = ec.element_to_be_clickable((self.get_search_condition(), self.get_locator()))
        return self.wait_for_check_by_condition(method_to_check=waiter, message=" не доступен для щелчка")

    def wait_for_is_visible(self):
        self.wait_for_is_present()
        waiter = ec.visibility_of_element_located((self.get_search_condition(), self.get_locator()))
        self.wait_for_check_by_condition(method_to_check=waiter, message=" не видим")

    def wait_for_is_present(self):
        waiter = ec.presence_of_element_located((self.get_search_condition(), self.get_locator()))
        self.wait_for_check_by_condition(method_to_check=waiter, message=" не существует")

    def wait_for_text(self, text, wait_time_sec=Waits.EXPLICITLY_WAIT_SEC):
        waiter = ec.text_to_be_present_in_element((self.get_search_condition(), self.get_locator()), text)
        self.wait_for_check_by_condition(method_to_check=waiter,
                                         message=" не содержит " + text, wait_time_sec=wait_time_sec)

    def wait_for_visibility(self):
        waiter = ec.visibility_of(self.find_element())
        self.wait_for_check_by_condition(method_to_check=waiter, message=" не стал видимым")

    def wait_for_check_by_condition(self, method_to_check, message,
                                    wait_time_sec=Waits.EXPLICITLY_WAIT_SEC, use_default_msg=True):
        try:
            element = WebDriverWait(Browser.get_browser().get_driver(), wait_time_sec).until(method=method_to_check)
        except TimeoutException:
            result_message = ("элемент '" + self.get_name() + "' с локатором " + self.get_locator() + message
                              if use_default_msg else message)
            Logger.warning(result_message)
            raise TimeoutException(result_message)
        return element
