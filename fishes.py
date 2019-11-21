"""
s
"""
import json
import random

import pool

X, Y = 0, 1


class Fish:
    """
    s
    """
    def __init__(self, x, y):
        """

        :param x:
        :param y:
        """
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

    def move(self, filled_pool: pool.Pool) -> None:
        """

        :param filled_pool:
        :return:
        """
        self._life_counter -= 1
        self._move(filled_pool)
        self.place_in_bounds(filled_pool)

    def _move(self, filled_pool: pool.Pool):
        """

        s
        """

    def is_alive(self):
        """

        :return:
        """
        return self._life_counter > 0

    def place_in_bounds(self, filled_pool: pool.Pool):
        """

        :param filled_pool:
        :return:
        """
        try:
            self._pos[X] = min(max(self._pos[X], 0), filled_pool.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), filled_pool.get_size()[Y] - 1)
        except ValueError:
            print("Oooops!")

    def born(self, filled_pool: pool.Pool):
        """

        :param filled_pool:
        :return:
        """
        if random.randint(1, 10) < self._born_rate:
            filled_pool.fill(self.__class__, self._born_num)


class Predator(Fish):
    """
    s
    """
    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x_pos, y_pos):
        """

        :param x_pos:
        :param y_pos:
        """
        super().__init__(x_pos, y_pos)
        self.__dict__.update(self.state)

    def _move(self, filled_pool: pool.Pool):
        """

        :param filled_pool:
        :return:
        """
        self._is_not_hungry -= 1
        victim = filled_pool.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, filled_pool: pool.Pool) -> None:
        """
        s
        """
        victims = filled_pool.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                filled_pool.kill(victim)

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
    s
    """
    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x_pos, y_pos):
        """

        :param x_pos:
        :param y_pos:
        """
        super().__init__(x_pos, y_pos)
        self.__dict__.update(self.state)

    def _move(self, _):
        """

        :param filled_pool:
        :return:
        """
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        """

        :return:
        """
        return "V"

    is_victim = lambda self: True


class Pick(Predator):
    """
    s
    """
    with open("pick.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x_pos, y_pos):
        """

        :param x_pos:
        :param y_pos:
        """
        super().__init__(x_pos, y_pos)
        self.__dict__.update(self.state)

    def _move(self, filled_pool: pool.Pool):
        """

        :param filled_pool:
        :return:
        """
        self._is_not_hungry -= 1
        victim = filled_pool.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2
