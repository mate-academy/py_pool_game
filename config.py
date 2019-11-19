"""Configuration parser"""
import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read('pool.ini')


def get_ticks():
    """return necessary data about pool size and number of fish"""
    return int(CONFIG['App']['Ticks'])
