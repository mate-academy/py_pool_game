""" Docstring """
import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read('pool.ini')


def get_ticks():
    """ Docstring """
    return int(CONFIG['App']['Ticks'])
