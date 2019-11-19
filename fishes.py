"""Module fishes"""
import json
import random

import pool

X, Y = 0, 1


class Fish:
    """Fish class"""

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

    def move(self, pol):
        """

        :param pol:
        :return:
        """
        self._life_counter -= 1
        self._move(pol)
        self.place_in_bounds(pol)

    def is_alive(self):
        """

        :return:
        """
        return self._life_counter > 0

    def _move(self, pol: pool.Pool):
        """

        :param pol:
        :return:
        """

    def place_in_bounds(self, pol):
        """

        :param pol:
        :return:
        """
        try:
            self._pos[X] = min(max(self._pos[X], 0), pol.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), pol.get_size()[Y] - 1)
        except ValueError:
            print("Oooops!")

    def eat(self, pol: pool.Pool):
        """

        :param pol:
        :return:
        """

    def born(self, pol: pool.Pool):
        """

        :param pol:
        :return:
        """
        if random.randint(1, 10) < self._born_rate:
            pol.fill(self.__class__, self._born_num)


class Predator(Fish):
    """Predator class"""
    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, pol=None):
        """

        :param pol:
        :return:
        """
        self._is_not_hungry -= 1
        victim = pol.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, pol: pool.Pool):
        """

        :param pol:
        :return:
        """
        victims = pol.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                pol.kill(victim)

    def __repr__(self):
        return "P"

    def is_alive(self):
        """

        :return:
        """
        return super().is_alive() and self._is_not_hungry > 0


class Pike(Predator):
    """Pike class"""
    with open("pike.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)


class Victim(Fish):
    """Victim class"""

    is_victim = True

    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, pol: pool.Pool):
        """

        :param pol:
        :return:
        """
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        return "V"
