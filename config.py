"""CONFIG"""
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('pool.ini')


def get_ticks():
    """get ticks"""
    return int(CONFIG['App']['Ticks'])
