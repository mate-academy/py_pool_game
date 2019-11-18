"""
module docstring
"""
import math
import random

import config

POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """class Pool"""

    def __init__(self):
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self._fishes = []

    def get_fishes(self):
        """

        :return:
        """
        return self._fishes

    def set_fishes(self, fishes):
        """

        :param fishes:
        :return:
        """
        self._fishes = fishes

    def get_size(self):
        """
        get size of pool
        :return:
        """
        return self._width, self._height

    def fill(self, fish_type, number: int):
        """
        method fill
        :param fish_type:
        :param number:
        :return:
        """
        self._fishes += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        """

        :return:
        """
        strng = '+' + '-' * self._width + '+\n'
        pool = [[' '] * self._width for _ in range(self._height)]
        for fish in self._fishes:
            pool[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in pool:
            strng += '|' + ''.join(row) + '|\n'
        strng += '+' + '-' * self._width + '+\n'
        return strng

    def tick(self):
        """

        :return:
        """
        for fish in self._fishes:
            fish.move(self)
            fish.eat(self)

        for fish in self._fishes.copy():
            if not fish.is_alive():
                self.kill(fish)
            else:
                fish.born(self)

    def get_nearest_victim(self, x_axis, y_axis):
        """
        get information about nearest victim in the pool
        :param x_axis: int
        :param y_axis: int
        :return: int
        """
        nearest_victims = [fish.get_pos()
                           for fish in self.get_fishes()
                           if fish.is_victim]
        if not nearest_victims:
            return 0, 0
        return tuple(min(nearest_victims,
                         key=lambda f:
                         math.hypot(f[0] - x_axis, f[1] - y_axis)))

    def get_victim(self, pos):
        """

        :param pos:
        :return:
        """
        return [fish for fish in self._fishes
                if fish.get_pos() == pos and fish.is_victim]

    def kill(self, victim):
        """

        :param victim:
        :return:
        """
        self._fishes.remove(victim)
