'''module'''
import random
import math
import config


POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    '''class'''
    def __init__(self):
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self._fishes = []

    def get_size(self):
        '''def'''
        return self._width, self._height

    def get_fishes(self):
        '''def'''
        return self._fishes

    def fill(self, fish_type, number: int):
        '''def'''
        self._fishes += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        '''def'''
        line = '+' + '-'*self._width + '+\n'
        swimming_pool = [[' ']*self._width for _ in range(self._height)]
        for fish in self._fishes:
            swimming_pool[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in swimming_pool:
            line += '|' + ''.join(row) + '|\n'
        line += '+' + '-'*self._width + '+\n'
        return line

    def tick(self):
        '''def'''
        for fish in self._fishes:
            fish.move(self)
            fish.eat(self)

        for fish in self._fishes.copy():
            if not fish.is_alive():
                self.kill(fish)
            else:
                for fishes in self._fishes.copy():
                    fishes.born(self)

    def get_nearest_victim(self, x_coord, y_coord):
        '''def'''
        nearest_victims = [fish.get_pos()
                           for fish in self._fishes if fish.is_victim]
        if not nearest_victims:
            return 0, 0
        return tuple(min(nearest_victims,
                         key=lambda f:
                         math.hypot(f[0] - x_coord, f[1] - y_coord)))

    def get_victim(self, pos):
        '''def'''
        return [fish for fish in self._fishes
                if fish.get_pos() == pos and fish.is_victim]

    def kill(self, victim):
        '''def'''
        self._fishes.remove(victim)
