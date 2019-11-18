"""This is docstring"""
import pool
import fishes

import config

if __name__ == "__main__":
    P = pool.Pool()
    P.fill(fishes.Predator, int(config.CONFIG["App"]["Predators"]))
    P.fill(fishes.Victim, int(config.CONFIG["App"]["Victims"]))
    for i in range(config.get_ticks()):
        print(P)
        P.tick()
