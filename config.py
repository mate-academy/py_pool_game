"""
  Z name main
  Nain jjk.
"""
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('pool.ini')


def get_ticks():
    """
      Z name main
      Nain jjk.
    """
    return int(CONFIG['App']['Ticks'])
