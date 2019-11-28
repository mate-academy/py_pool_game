"""pool init"""


import random
import math
import config

POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """pool object"""
    def __init__(self):
        """init pool"""
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self.fishes = []

    def get_size(self):
        """return size of pool"""
        return self._width, self._height

    def fill(self, fish_type, number: int):
        """i don`t know"""
        self.fishes += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        """printing"""
        sls = '+' + '-' * self._width + '+\n'
        prd = [[' '] * self._width for _ in range(self._height)]
        for fish in self.fishes:
            prd[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in prd:
            sls += '|' + ''.join(row) + '|\n'
        sls += '+' + '-' * self._width + '+\n'
        return sls

    def tick(self):
        """tock"""
        for fish in self.fishes:
            fish.move(self)
            fish.eat(self)

        for fish in self.fishes.copy():
            if not fish.is_alive():
                self.kill(fish)
                break
        else:
            for fish in self.fishes.copy():
                fish.born(self)

    def get_nearest_victim(self, xcc, ycc):
        """retrun nearest victim"""
        nearest_victims = [fish.get_pos()
                           for fish in self.fishes if fish.is_victim()]
        if not nearest_victims:
            return (0, 0)
        return tuple(min(nearest_victims,
                         key=lambda f: math.hypot(f[0] - xcc, f[1] - ycc)))

    def get_victim(self, pos):
        """return victim"""
        return [fish for fish in self.fishes
                if fish.get_pos() == pos and fish.is_victim()]

    def kill(self, victim):
        """kill somebody"""
        self.fishes.remove(victim)
