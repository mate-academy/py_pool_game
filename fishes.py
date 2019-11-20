"""This is module docstring"""
import json
import random


import pool

X, Y = 0, 1


class Fish:
    """This is Class docstring"""

    def __init__(self, x, y):
        self._pos = [x, y]
        self._life_counter = 10
        self._born_rate = 0
        self._born_num = 0
        self._is_not_hungry = 0

    def get_pos(self):
        """This is method docstring"""
        return self._pos

    def move(self, sw_pool):
        """This is method docstring"""
        self._life_counter -= 1
        self._move(sw_pool)
        self.place_in_bounds(sw_pool)

    def is_alive(self):
        """This is method docstring"""
        return self._life_counter > 0

    def _move(self, sw_pool: pool.Pool):
        """This is method docstring"""
        # TO DO

    @property
    def is_victim(self) -> bool:
        """This is method docstring"""
        return False

    def place_in_bounds(self, sw_pool):
        """This is method docstring"""
        try:
            self._pos[X] = min(max(self._pos[X], 0), sw_pool.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), sw_pool.get_size()[Y] - 1)
        except ValueError:
            print("Oooops!")

    def eat(self, sw_pool: pool.Pool):
        """This is method docstring"""

    def born(self, sw_pool: pool.Pool):
        """This is method docstring"""
        if random.randint(1, 10) < self._born_rate:
            sw_pool.fill(self.__class__, self._born_num)


class Predator(Fish):
    """This is method docstring"""
    with open("predator.json", "rt") as f:
        state = json.load(f)

    with open("predator.json", "rt") as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, sw_pool):
        self._is_not_hungry -= 1
        victim = sw_pool.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, sw_pool: pool.Pool):
        """This is method docstring"""
        victims = sw_pool.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                sw_pool.kill(victim)

    def __repr__(self):
        return "P"

    def is_alive(self):
        return super().is_alive() and self._is_not_hungry > 0


class Victim(Fish):
    """This is class docstring"""
    with open("victim.json", "rt") as f:
        state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, sw_pool):
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        return "V"

    @property
    def is_victim(self):
        return lambda self: True
