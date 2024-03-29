# coding=utf-8
from __future__ import annotations

import webbrowser


from selenium.common.exceptions import NoSuchWindowException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from framework.singleton import Singleton
from framework.utils.logger import Logger
from tests.config.browser import BrowserConfig
from tests.config.waits import Waits
from .browser_factory import BrowserFactory


class Browser(metaclass=Singleton):
    def __init__(self) -> None:
        self.__web_driver = {}
        self.__main_window_handle = None
        self.__selected_browser = BrowserConfig.BROWSER

    @staticmethod
    def get_browser() -> Browser:
        return Browser()

    def get_selected_browser_key(self) -> str:
        return self.__selected_browser

    def get_browser_keys(self) -> dict.keys:
        return self.__web_driver.keys()

    def get_driver(self) -> webbrowser:
        return self.__web_driver[self.__selected_browser]

    def set_up_driver(self, browser_key: str = BrowserConfig.BROWSER, capabilities: str | None = None,
                      is_incognito: bool = False, enable_performance_logging: bool = False) -> None:
        Logger.info('Инициализация драйвера для браузера ' + BrowserConfig.BROWSER)
        if browser_key in self.__web_driver:
            raise ValueError("Браузер с  ключом '{}', уже создан.".format(browser_key))
        self.__web_driver[browser_key] = \
            BrowserFactory.get_browser_driver(capabilities=capabilities,
                                              is_incognito=is_incognito,
                                              enable_performance_logging=enable_performance_logging)
        self.__web_driver[browser_key].implicitly_wait(Waits.IMPLICITLY_WAIT_SEC)
        self.__web_driver[browser_key].set_page_load_timeout(Waits.PAGE_LOAD_TIMEOUT_SEC)
        self.__web_driver[browser_key].set_script_timeout(Waits.SCRIPT_TIMEOUT_SEC)
        self.__main_window_handle = self.__web_driver[browser_key].current_window_handle
        self.select_browser(browser_key)

    def select_browser(self, browser_key: str = BrowserConfig.BROWSER) -> None:
        if browser_key not in self.__web_driver:
            raise KeyError("Браузер с  ключом '{}', не существует.".format(browser_key))
        self.__selected_browser = browser_key

    def quit(self, browser_key: str = BrowserConfig.BROWSER) -> None:
        browser_inst = self.__web_driver.get(browser_key)
        if browser_inst is not None:
            Logger.info("Завершение работы драйвера")
            browser_inst.quit()
            self.__web_driver.pop(browser_key, None)

    def get_driver_names(self) -> dict.keys:
        return self.__web_driver.keys()

    def close(self, page_name: str = "") -> None:
        if self.get_driver() is not None:
            Logger.info("Закрытие страницы %s " % page_name)
            self.get_driver().close()

    def refresh_page(self) -> None:
        Logger.info("Перезагрузка страницы")
        self.get_driver().refresh()

    def maximize(self, browser_key: str = BrowserConfig.BROWSER) -> None:
        self.__web_driver[browser_key].maximize_window()

    def set_url(self, url: str) -> None:
        Logger.info("Изменение url страницы на " + url)
        self.get_driver().get(url)

    def get_cookies(self) -> str:
        Logger.info("Получение всех cookies")
        return self.get_driver().get_cookies()

    def get_cookie(self, name: str) -> str:
        Logger.info("Получение cookie с именем: " + name)
        return self.get_driver().get_cookie(name=name)

    def get_current_url(self) -> str:
        return self.get_driver().current_url

    def back_page(self) -> None:
        self.get_driver().back()

    def switch_to_window(self, window_handle: None | object = None) -> bool | None:
        if window_handle is None:
            window_handle = self.__main_window_handle
        Logger.info("Переключение на окно с именем %s" % window_handle)
        try:
            self.get_driver().switch_to_window(window_handle)
        except NoSuchWindowException:
            Logger.error("Не найдено подходящее окно с менем %s" % window_handle)
            return False

    def get_count_windows(self) -> int:
        count = len(self.get_driver().window_handles)
        Logger.info("Количество открытых окон браузера: %d" % count)
        return count

    def switch_new_window(self, logged_page_name: str = "") -> None:
        Logger.info("Переключение на новое окно %s" % logged_page_name)
        handles = self.get_driver().window_handles
        if len(handles) <= 1:
            raise NoSuchWindowException("Нет нового окна. Количество окон равно %s" % len(handles))
        self.get_driver().switch_to_window(handles[-1])

    def switch_to_frame_by_name(self, frame_name: str) -> None:
        Logger.info("Переключение на фрейм с именем %s" % frame_name)
        self.get_driver().switch_to_frame(frame_name)

    def switch_to_frame_by_locator(self,
                                   search_condition: str,
                                   locator: str) -> None:
        Logger.info("Переключение на фрейм локатором {}".format(locator))
        self.get_driver().switch_to.frame(self.get_driver().find_element(search_condition, locator))

    def switch_to_default_content(self) -> None:
        Logger.info("Переключение на главный фрейм")
        self.get_driver().switch_to_default_content()

    def wait_for_check_by_condition(self, waiter: int,
                                    time_in_seconds: int = Waits.IMPLICITLY_WAIT_SEC,
                                    message: str = "") -> None:
        try:
            WebDriverWait(self.get_driver(), time_in_seconds).until(waiter)
        except TimeoutException:
            error_msg = "По истечении {time} секунд не выполнено событие: {msg}".format(time=time_in_seconds,
                                                                                        msg=message)
            Logger.warning(error_msg)
            raise TimeoutException(error_msg)

    @staticmethod
    def is_wait_successful(wait_function, *args) -> bool:
        try:
            wait_function(*args)
        except TimeoutException:
            return False
        return True

    def add_cookie(self, cookie_name: str, cookie_value: str) -> None:
        self.get_driver().add_cookie({'name': cookie_name,
                                      'value': cookie_value})
