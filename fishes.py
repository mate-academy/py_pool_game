"""
docstring
"""
import json
import random

import pool

X, Y = 0, 1


class Fish:
    """
    Fish class
    """

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

    def move(self, pas: pool.Pool):
        """

        :param pas:
        :return:
        """
        self._life_counter -= 1
        return self._move(pas), self.place_in_bounds(pas)

    def is_alive(self):
        """

        :return:
        """
        return self._life_counter > 0

    def _move(self, pas: pool.Pool):
        """

        :param pas:
        :return:
        """

    def place_in_bounds(self, pas: pool.Pool):
        """

        :param pas:
        :return:
        """
        try:
            self._pos[X] = min(max(self._pos[X], 0), pas.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), pas.get_size()[Y] - 1)
        except ValueError:
            print("Oops!")

    def eat(self, pas: pool.Pool):
        """

        :param pas:
        :return:
        """

    def born(self, pas: pool.Pool):
        """

        :param pas:
        :return:
        """
        if random.randint(1, 10) < self._born_rate:
            pas.fill(self.__class__, self._born_num)


class Predator(Fish):
    """
    Predator class
    """

    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, pas=None):
        """

        :param pas:
        :return:
        """
        self._is_not_hungry -= 1
        victim = pas.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, pas: pool.Pool):
        """

        :param pas:
        :return:
        """
        victims = pas.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                pas.kill(victim)

    def __repr__(self):
        """

        :return:
        """
        return "P"

    def is_alive(self):
        """

        :return:
        """
        return super().is_alive() and self._is_not_hungry > 0


class Victim(Fish):
    """
    docstring
    """

    is_victim = True

    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        """

        :param x:
        :param y:
        """
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, pas: pool.Pool):
        """

        :param pas:
        :return:
        """
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        """

        :return:
        """
        return "V"


class Pike(Predator):
    """
    Pike class
    """

    with open("pike.json", 'rt') as f:
        state = json.load(f)

    with open("pike.json", 'rt') as f:
        predator_state = json.load(f)
