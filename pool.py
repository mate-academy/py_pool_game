"""modules """
import random

import math

import config

POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """pool"""
    def __init__(self):
        """  """
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self._fishes = []

    def get_size(pool):
        """get size"""
        return pool._width, pool._height

    def fill(self, fish_type, number: int):
        """ fill"""
        self._fishes += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        """something"""
        sss = '+' + '-'*self._width + '+\n'
        poo = [[' ']*self._width for _ in range(self._height)]
        for fish in self._fishes:
            poo[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in poo:
            sss += '|' + ''.join(row) + '|\n'
        sss += '+' + '-'*self._width + '+\n'
        return sss

    def tick(self):
        """tick"""
        for fish in self._fishes:
            fish.move(self)
            fish.eat(self)

        for fish in self._fishes.copy():
            if not fish.is_alive():
                self.kill(fish)
                break
        else:
            for fish in self._fishes.copy():
                fish.born(self)

    def get_nearest_victim(self, xcor, ycor):
        """victim"""
        nearest_victims = [fish.get_pos() for fish in self._fishes
                           if fish.is_victim()]
        if not nearest_victims:
            return (0, 0)
        return tuple(min(nearest_victims,
                         key=lambda f: math.hypot(f[0] - xcor, f[1] - ycor)))

    def get_victim(self, pos):
        """victim"""
        return [fish for fish in self._fishes
                if fish.get_pos() == pos and fish.is_victim()]

    def kill(self, victim):
        """kill"""
        self._fishes.remove(victim)
