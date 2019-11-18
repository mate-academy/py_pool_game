import random
import types

import config

import math

POOL_WIDTH = int(config.config['Pool']['Width'])
POOL_HEIGHT = int(config.config['Pool']['Height'])


class Pool:
    def __init__(self):
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self._fishes = []

    def get_size(self,):
        return self._width, self._height

    def fill(self, fish_type, number: int):
        self._fishes += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        s = '+' + '-'*self._width + '+\n'
        p = [[' ']*self._width for _ in range(self._height)]
        for fish in self._fishes:
            p[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in p:
            s += '|' + ''.join(row) + '|\n'
        s += '+' + '-'*self._width + '+\n'
        return s

    def tick(self):
        for fish in self._fishes:
            fish.move(self)
            fish.eat(self)

        for fish in self._fishes.copy():
            if not fish.is_alive():
                self.kill(fish)
        else:
            for fish in self._fishes.copy():
                fish.born(self)

    def get_nearest_victim(self, x, y):
        nearest_victims = [fish.get_pos()
                           for fish in self._fishes if fish.is_victim()]
        if not nearest_victims:
            return 0, 0
        return tuple(min(
            nearest_victims, key=lambda f: math.hypot(f[0] - x, f[1] - y)))

    def get_victim(self, pos):
        return [fish for fish in self._fishes
                if fish.get_pos() == pos and fish.is_victim()]

    def kill(self, victim):
        self._fishes.remove(victim)
