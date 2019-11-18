"""Config description"""
import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read('pool.ini')


def get_ticks():
    """Get app ticks from config"""
    return int(CONFIG['App']['Ticks'])
