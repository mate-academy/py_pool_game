
import pool
import fishes

import config

if __name__ == '__main__':
    p = pool.Pool()
    p.fill(fishes.Predator, int(config.config['App']['Predators']))
    p.fill(fishes.Victim, int(config.config['App']['Victims']))
    for i in range(config.get_ticks()):
        print(p)
        p.tick()