"""
s
"""
import math
import random

import config

from is_victim import is_victim

POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """
    s
    """
    def __init__(self):
        """
        s
        """
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self._fishes = []

    def get_fishes(self):
        """

        :return:
        """
        return self._fishes

    fishes = property(get_fishes)

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
        string = '+' + '-' * self._width + '+\n'
        pool_filling = [[' '] * self._width for _ in range(self._height)]
        for fish in self._fishes:
            pool_filling[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in pool_filling:
            string += '|' + ''.join(row) + '|\n'
        string += '+' + '-' * self._width + '+\n'
        return string

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
                break
        else:
            for fish in self._fishes.copy():
                fish.born(self)

    def get_nearest_victim(self, x_pos, y_pos):
        """

        :param x_pos:
        :param y_pos:
        :return:
        """
        nearest_victims = [fish.get_pos() for fish in self._fishes if is_victim(fish)]
        if not nearest_victims:
            return (0, 0)
        return tuple(min(nearest_victims, key=lambda f: math.hypot(f[0] - x_pos, f[1] - y_pos)))

    def get_victim(self, pos):
        """

        :param pos:
        :return:
        """
        return [fish for fish in self._fishes if fish.get_pos() == pos and is_victim(fish)]

    def kill(self, victim):
        """

        :param victim:
        :return:
        """
        self._fishes.remove(victim)
