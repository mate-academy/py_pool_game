"""DOCSTRING"""
import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read('pool.ini')


def get_ticks():
    """DOCSTRING"""
    return int(CONFIG['App']['Ticks'])
