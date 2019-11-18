"""
About fishes
"""
import random
import json

import pool

X, Y = 0, 1


class Fish:
    """
    class fish
    """
    def __init__(self, x, y):
        self._pos = [x, y]
        self._life_counter = 10
        self._born_rate = 0
        self._born_num = 0
        self._is_not_hungry = 0

    is_victim = False

    def get_pos(self):
        """
            get fish position
        """
        return self._pos

    def move(self, how):
        """
            fish moving
        """
        self._life_counter -= 1
        self._move(how)
        self.place_in_bounds(how)

    def is_alive(self):
        """
            are fish alive?
        """
        return self._life_counter > 0

    def _move(self, how: pool.Pool):
        pass

    def place_in_bounds(self, place):
        """
            place in bounds
        """
        try:
            self._pos[X] = min(max(self._pos[X], 0), place.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), place.get_size()[Y] - 1)
        except ValueError:
            print("Oooops!")

    def eat(self, pooler: pool.Pool):
        """DOCSTRING"""

    def born(self, eat: pool.Pool):
        """
            born
        """
        if random.randint(1, 10) < self._born_rate:
            eat.fill(self.__class__, self._born_num)


class Predator(Fish):
    """
        class predator
    """
    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, how):
        self._is_not_hungry -= 1
        victim = how.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, pooler: pool.Pool):
        """
        eat
        """
        victims = pooler.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                pooler.kill(victim)

    def __repr__(self):
        return "P"

    def is_alive(self):
        return super().is_alive() and self._is_not_hungry > 0


class Victim(Fish):
    """VICTIM"""
    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    is_victim = True

    def _move(self, how):
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        return "V"


class Pike(Predator):
    """
    class Pike
    """
    with open("pike.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)
