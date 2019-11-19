'''module'''
import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read('pool.ini')


def get_ticks():
    '''def'''
    return int(CONFIG['App']['Ticks'])
