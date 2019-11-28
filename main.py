""" main module"""


import pool
import fishes

import config

if __name__ == '__main__':
    POO = pool.Pool()
    POO.fill(fishes.Predator, int(config.CONFIG['App']['Predators']))
    POO.fill(fishes.Victim, int(config.CONFIG['App']['Victims']))
    for i in range(config.get_ticks()):
        print(POO)
        POO.tick()
