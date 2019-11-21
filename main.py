"""MAIN"""
import pool
import fishes

import config

if __name__ == '__main__':
    P_N = pool.Pool()
    P_N.fill(fishes.Predator, int(config.CONFIG['App']['Predators']))
    P_N.fill(fishes.Victim, int(config.CONFIG['App']['Victims']))
    for i in range(config.get_ticks()):
        print(P_N)
        P_N.tick()
