"""Module Pool"""
import random
import math

import config

POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """Pool class"""
    def __init__(self):
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self.fish_in_pool = []

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
        self.fish_in_pool += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        line = '+' + '-' * self._width + '+\n'
        pol = [[' '] * self._width for _ in range(self._height)]
        for fish in self.fish_in_pool:
            pol[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in pol:
            line += '|' + ''.join(row) + '|\n'
        line += '+' + '-' * self._width + '+\n'
        return line

    def tick(self):
        """

        :return:
        """
        for fish in self.fish_in_pool:
            fish.move(self)
            fish.eat(self)

        for fish in self.fish_in_pool.copy():
            if not fish.is_alive():
                self.kill(fish)

        for fish in self.fish_in_pool.copy():
            fish.born(self)

    def get_nearest_victim(self, x_coord, y_coord):
        """

        :param x_coord:
        :param y_coord:
        :return:
        """
        nearest_victims = [fish.get_pos() for fish in self.fish_in_pool
                           if fish.is_victim]
        if not nearest_victims:
            return (0, 0)
        return tuple(min(nearest_victims, key=lambda f:
                         math.hypot(f[0] - x_coord, f[1] - y_coord)))

    def get_victim(self, pos):
        """

        :param pos:
        :return:
        """
        return [fish for fish in self.fish_in_pool
                if fish.get_pos() == pos and fish.is_victim]

    def kill(self, victim):
        """

        :param victim:
        :return:
        """
        self.fish_in_pool.remove(victim)
