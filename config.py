"""This is docstring"""
import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read("pool.ini")


def get_ticks():
    """This is function docstring"""
    return int(CONFIG["App"]["Ticks"])
