"""import"""
import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read('pool.ini')


def get_ticks():
    """return"""
    return int(CONFIG['App']['Ticks'])
