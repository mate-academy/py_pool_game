"""Execute all modules"""
import pool
import fishes

import config

if __name__ == '__main__':
    NEW_POOL = pool.Pool()
    NEW_POOL.fill(fishes.Predator, int(config.CONFIG['App']['Predators']))
    NEW_POOL.fill(fishes.Victim, int(config.CONFIG['App']['Victims']))
    for i in range(config.get_ticks()):
        print(NEW_POOL)
        NEW_POOL.tick()
