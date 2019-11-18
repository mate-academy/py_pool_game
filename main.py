"""Main module description"""
import pool
import fishes

import config

if __name__ == '__main__':

    PLACE = pool.Pool()
    PLACE.fill(fishes.Predator, int(config.CONFIG['App']['Predators']))
    PLACE.fill(fishes.Victim, int(config.CONFIG['App']['Victims']))
    for i in range(config.get_ticks()):
        print(PLACE)
        PLACE.tick()
