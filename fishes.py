"""This module defines Fish class
and two subclasses of Fish class: Victim and Predator"""
import json
import random

import pool

X, Y = 0, 1


class Fish:
    """This is general class for all types of fish"""
    def __init__(self, x, y):
        self._pos = [x, y]
        self._life_counter = 10
        self._born_rate = 0
        self._born_num = 0
        self._is_not_hungry = 0

    def get_pos(self):
        """return fish position"""
        return self._pos

    def move(self, new_pool: pool.Pool):
        """moves fish and subtract 1 life"""
        self._life_counter -= 1
        self._move(new_pool)
        self.place_in_bounds(new_pool)

    def is_alive(self):
        """IT'S ALIVE!!! ALIVE!...isn't?"""
        return self._life_counter > 0

    def _move(self, new_pool: pool.Pool):
        """Later we will make smth essential"""

    def place_in_bounds(self, pool_inst):
        """define a fish position"""
        try:
            self._pos[X] = min(max(self._pos[X], 0),
                               pool_inst.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0),
                               pool_inst.get_size()[Y] - 1)
        except ValueError:
            print("Oooops!")

    def eat(self, new_pool: pool.Pool):
        """Later we will make smth essential"""

    def born(self, new_pool: pool.Pool):
        """makes new fish"""
        if random.randint(1, 10) < self._born_rate:
            new_pool.fill(self.__class__, self._born_num)


class Predator(Fish):
    """This is subclass of the Fish class - Predator.
    They love the taste of fish"""
    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, new_pool: pool.Pool):
        self._is_not_hungry -= 1
        victim = new_pool.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, new_pool: pool.Pool):
        """Eat, eat, eat..."""
        victims = new_pool.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                new_pool.kill(victim)

    def __repr__(self):
        return "P"

    def is_alive(self):
        return super().is_alive() and self._is_not_hungry > 0

    @staticmethod
    def is_victim() -> bool:
        """Is it victim?"""
        return False


class Victim(Fish):
    """This is subclass of the Fish class - Victim.
        They don't have method like 'eat'"""
    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, new_pool: pool.Pool):
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        return "V"

    @staticmethod
    def is_victim() -> bool:
        """Is it victim?"""
        return True
