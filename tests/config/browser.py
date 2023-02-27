from framework.utils.config_parser import ConfigParser

CONFIG = ConfigParser().get_config()


class BrowserConfig(object):
    BROWSER = CONFIG['browser']
    LOCALIZATION = CONFIG['lang']
