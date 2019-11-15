import random
import json
import random

import pool

X, Y = 0, 1


class Fish:
    def __init__(self, x, y):
        self._pos = [x, y]
        self._life_counter = 10
        self._born_rate = 0
        self._born_num = 0
        self._is_not_hungry = 0

    def get_pos(self):
        return self._pos

    def move(self, p: pool.Pool) -> tuple:
        self._life_counter -= 1
        self._move(p)
        self.place_in_bounds(p)

    def is_alive(self):
        return self._life_counter > 0

    def _move(self, p: pool.Pool):
        pass

    def is_victim(self) -> bool:
        return False

    def place_in_bounds(self, p: list):
        try:
            self._pos[X] = min(max(self._pos[X], 0), p.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), p.get_size()[Y] - 1)
        except Exception:
            pass
        except ValueError:
            print("Oooops!")

    def eat(self, p: pool.Pool):
        pass

    def born(self, p: pool.Pool):
        if random.randint(1, 10) < self._born_rate:
            p.fill(self.__class__, self._born_num)


class Predator(Fish):
    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, p: pool.Pool=[]):
        self._is_not_hungry -= 1
        victim = p.get_nearest_victim(*self._pos)
        self._pos[X]+= 2 if victim[X]>self._pos[X] else -2
        self._pos[Y]+= 2 if victim[Y]>self._pos[Y] else -2

    def eat(self, p: pool.Pool) -> int:
        """
        """
        victims = p.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                p.kill(victim)

    def __repr__(self):
        return "P"

    def is_alive(self):
        return super().is_alive() and self._is_not_hungry > 0


class Victim(Fish):
    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, p: pool.Pool):
        self._pos[X] += random.randint(-1,1)
        self._pos[Y] += random.randint(-1,1)

    def __repr__(self):
        return "V"

    is_victim = lambda self: True
