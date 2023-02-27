# coding=utf-8

from os import environ

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from framework.constants import browsers
from tests.config.browser import BrowserConfig


class BrowserFactory:

    @staticmethod
    def get_browser_driver(capabilities=None, is_incognito=False, enable_performance_logging=False, test_name=None,
                           grid_port=None):
        if capabilities is None:
            capabilities = {}
        if BrowserConfig.BROWSER == browsers.BROWSER_CHROME:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option('w3c', False)
            chrome_options.add_argument("--lang={}".format(BrowserConfig.LOCALIZATION))

            if is_incognito:
                chrome_options.add_argument("--incognito")
            if enable_performance_logging:
                capabilities['loggingPrefs'] = {'performance': 'ALL'}
            else:
                return webdriver.Chrome(ChromeDriverManager().install(),
                                        options=chrome_options,
                                        desired_capabilities=capabilities)

        elif BrowserConfig.BROWSER == browsers.BROWSER_FIREFOX:
            firefox_profile = webdriver.FirefoxProfile()
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--lang={}".format(BrowserConfig.LOCALIZATION))
            if is_incognito:
                firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
            if enable_performance_logging:
                open("perfLog.txt", "w").close()
                environ["MOZ_LOG"] = "timestamp,sync,nsHttp:3"
            else:
                return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                         firefox_profile=firefox_profile,
                                         desired_capabilities=capabilities, options=firefox_options)
