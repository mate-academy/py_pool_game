"""
docstring
"""

import math
import random

import config

POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """
    Pool class
    """

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

        :return:
        """
        return self._width, self._height

    def fill(self, fish_type, number: int):
        """

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
        strg = '+' + '-' * self._width + '+\n'
        pool = [[' '] * self._width for _ in range(self._height)]
        for fish in self._fishes:
            pool[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in pool:
            strg += '|' + ''.join(row) + '|\n'
        strg += '+' + '-' * self._width + '+\n'
        return strg

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

    def get_nearest_victim(self, x_ax, y_ax):
        """
        search for a victim on x and y axis
        :param y_ax: int
        :param x_ax: int
        :return:
        """
        nearest_victims = [fish.get_pos() for fish
                           in self.get_fishes() if fish.is_victim]
        if not nearest_victims:
            return 0, 0
        return tuple(min(nearest_victims,
                         key=lambda f: math.hypot(f[0] - x_ax, f[1] - y_ax)))

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
