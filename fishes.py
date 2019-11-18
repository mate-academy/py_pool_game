"""
module docstring
"""

import json
import random

import pool

X, Y = 0, 1


class Fish:
    """class docstring"""

    is_victim = False

    def __init__(self, x, y):
        self._pos = [x, y]
        self._life_counter = 10
        self._born_rate = 0
        self._born_num = 0
        self._is_not_hungry = 0

    def get_pos(self):
        """

        :return:
        """
        return self._pos

    def move(self, basin: pool.Pool) -> tuple:
        """

        :param pool:
        :return:
        """
        self._life_counter -= 1
        return self._move(basin), self.place_in_bounds(basin)

    def is_alive(self):
        """

        :return:
        """
        return self._life_counter > 0

    def _move(self, basin: pool.Pool):
        """

        :param basin:
        :return:
        """

    def place_in_bounds(self, basin: pool.Pool):
        """

        :param basin:
        :return:
        """
        try:
            self._pos[X] = min(max(self._pos[X], 0), basin.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), basin.get_size()[Y] - 1)
        except ValueError:
            print("Oooops!")

    def eat(self, basin: pool.Pool):
        """

        :param basin:
        :return:
        """

    def born(self, basin: pool.Pool):
        """

        :param basin:
        :return:
        """
        if random.randint(1, 10) < self._born_rate:
            basin.fill(self.__class__, self._born_num)


class Predator(Fish):
    """class docstring"""
    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, basin=None):
        """

        :param basin:
        :return:
        """
        if basin is None:
            basin = []
        self._is_not_hungry -= 1
        victim = basin.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, basin: pool.Pool):
        """

        :param pool:
        :return:
        """
        victims = basin.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                basin.kill(victim)

    def __repr__(self):
        return "P"

    def is_alive(self):
        """

        :return:
        """
        return super().is_alive() and self._is_not_hungry > 0


class Pike(Predator):
    """class docstring"""
    with open("pike.json", 'rt') as f:
        state = json.load(f)

    with open('pike.json', 'rt') as f:
        predator_state = json.load(f)


class Victim(Fish):
    """class docstring"""

    is_victim = True

    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, basin: pool.Pool):
        """

        :param basin:
        :return:
        """
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        return "V"
