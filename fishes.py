"""modules for our program"""
import json
import random

import pool

X, Y = 0, 1


class Fish:
    """ fish"""
    def __init__(self, x, y):
        self._pos = [x, y]
        self._life_counter = 10
        self._born_rate = 0
        self._born_num = 0
        self._is_not_hungry = 0

    def get_pos(self):
        """return position"""
        return self._pos

    def move(self, poo: pool.Pool) -> tuple:
        """moving"""
        self._life_counter -= 1
        self._move(poo)
        self.place_in_bounds(poo)


    def is_alive(self):
        """live or dead"""
        return self._life_counter > 0

    def is_victim(self) -> bool:
        """victim"""
        return False

    def place_in_bounds(self, poo: list):
        """place in bounds"""
        try:
            self._pos[X] = min(max(self._pos[X], 0), poo.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), poo.get_size()[Y] - 1)
        except ValueError:
            print("Oooops!")

    def born(self, poo: pool.Pool):
        """born"""
        if random.randint(1, 10) < self._born_rate:
            poo.fill(self.__class__, self._born_num)


class Predator(Fish):
    """predator fish"""
    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        """   """
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, poo: pool.Pool = None):
        """move"""
        self._is_not_hungry -= 1
        victim = poo.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, poo: pool.Pool) -> int:
        """
        eat
        """
        victims = poo.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                poo.kill(victim)

    def __repr__(self):
        """return"""
        return "P"

    def is_alive(self):
        """dead or alive"""
        return super().is_alive() and self._is_not_hungry > 0


class Victim(Fish):
    """victim fish"""
    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        """  """
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, poo: pool.Pool):
        """ move"""
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        """return"""
        return "V"

    def is_victim(self):
        """victim"""
        return True


class Pike(Predator):
    """pike predator fish"""
    with open("pike.json", 'rt') as f:
        state = json.load(f)

    with open('pike.json', 'rt') as f:
        predator_state = json.load(f)
