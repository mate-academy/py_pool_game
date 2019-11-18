"""Fishes module with fish and victim."""
import random
import json
from typing import Type

import pool

X, Y = 0, 1


class Fish:
    """Fish class that describes the behavior of a fish."""
    def __init__(self, x, y):
        self._pos = [x, y]
        self._life_counter = 10
        self._born_rate = 0
        self._born_num = 0
        self._is_not_hungry = 0

    def get_pos(self):
        """Function returns pos."""
        return self._pos

    def move(self, place: pool.Pool):
        """Move a fish"""
        self._life_counter -= 1
        self._move(place)
        self.place_in_bounds(place)

    def is_alive(self):
        """Fish status of life"""
        return self._life_counter > 0

    def _move(self, place: pool.Pool):
        """Do move"""

    @staticmethod
    def is_victim():
        """Fish is not victim"""
        return False

    def place_in_bounds(self, place: pool.Pool):
        """Bounds of a place"""
        try:
            self._pos[X] = min(max(self._pos[X], 0), place.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), place.get_size()[Y] - 1)
        except ValueError:
            print("Oooops!")

    def eat(self, place: pool.Pool):
        """Eat as a fish"""

    def born(self, place: pool.Pool):
        """Create a fish"""
        if random.randint(1, 10) < self._born_rate:
            place.fill(self.__class__, self._born_num)


class Predator(Fish):
    """Fish-predator class"""
    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        """Predator constructor"""
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, place: pool.Pool):
        """Move a predator"""
        self._is_not_hungry -= 1
        victim = place.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, place: pool.Pool) -> Type[int]:
        """eat a victim"""
        victims = place.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                place.kill(victim)
        return int

    def __repr__(self):
        """:return smth"""
        return "P"

    def is_alive(self):
        """Define if Predator is alive and not hungry"""
        return super().is_alive() and self._is_not_hungry > 0


class Victim(Fish):
    """Fish-victim class"""
    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        """Victim constructor"""
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, place: pool.Pool):
        """Move a victim fish"""
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        """don't know what is it"""
        return "V"

    def is_victim(self):
        """Victim fish"""
        return True
