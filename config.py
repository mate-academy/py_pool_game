import configparser


config = configparser.ConfigParser()
config.read('pool.ini')


def get_ticks():
    return int(config['App']['Ticks'])
