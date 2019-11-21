"""
Fishes modules
"""
import json
import random
import pool

X, Y = 0, 1


class Fish:
    """class fish"""
    def __init__(self, x, y):
        self._pos = [x, y]
        self._life_counter = 10
        self._born_rate = 0
        self._born_num = 0
        self._is_not_hungry = 0

    def get_pos(self):
        '''get_pos'''
        return self._pos

    def move(self, p_name: pool.Pool):
        """move"""
        self._life_counter -= 1
        self._move(p_name)
#        self.place_in_bounds(p)

    def is_alive(self):
        """is alive"""
        return self._life_counter > 0

    def _move(self, p_name: pool.Pool):
        """move"""

    @classmethod
    def is_victim(cls):
        """is victim"""
        return False

    def place_in_bounds(self, p_name: pool.Pool):
        """place in bound"""
        try:
            self._pos[X] = min(max(self._pos[X], 0), p_name.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), p_name.get_size()[Y] - 1)
        except SystemError:
            pass
        except ValueError:
            print("Oooops!")

    def eat(self, p_name: pool.Pool):
        """eat"""

    def born(self, p_name: pool.Pool):
        """born"""
        if random.randint(1, 10) < self._born_rate:
            p_name.fill(self.__class__, self._born_num)


class Predator(Fish):
    """predator"""
    with open("predator.json", 'rt') as f_:
        state = json.load(f_)

    with open('predator.json', 'rt') as f_:
        predator_state = json.load(f_)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, p_name: pool.Pool):
        self._is_not_hungry -= 1
        victim = p_name.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, p_name: pool.Pool):
        victims = p_name.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                p_name.kill(victim)

    def __repr__(self):
        return "P"

    def is_alive(self):
        """is alive"""
        return super().is_alive() and self._is_not_hungry > 0


class Victim(Fish):
    """victim"""
    with open("victim.json", 'rt') as f_name:
        state = json.load(f_name)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, p_name: pool.Pool):
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        return "V"

#    is_victim = lambda self: True

    def is_victim(self):
        return True


class Pike(Predator):
    """new pike class"""
    with open("pike.json", 'rt') as f_:
        state = json.load(f_)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__dict__.update(self.state)
