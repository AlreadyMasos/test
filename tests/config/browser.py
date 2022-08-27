from framework.utils.config_parser import ConfigParser

CONFIG = ConfigParser().get_config()


class BrowserConfig(object):
    BROWSER = CONFIG['browser']
    LOCALIZATION = CONFIG['lang']
    CHROME_VERSION = ""
    FIREFOX_VERSION = ""


class Grid(object):
    USE_GRID = False
    GRID_URL = ""
    GRID_HOST = ""