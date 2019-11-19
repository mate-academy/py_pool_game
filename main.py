'''class'''
import pool
import fishes
import config

if __name__ == '__main__':
    SWIMMING_POOL = pool.Pool()
    SWIMMING_POOL.fill(fishes.Predator, int(config.CONFIG['App']['Predators']))
    SWIMMING_POOL.fill(fishes.Victim, int(config.CONFIG['App']['Victims']))
    for i in range(config.get_ticks()):
        print(SWIMMING_POOL)
        SWIMMING_POOL.tick()
