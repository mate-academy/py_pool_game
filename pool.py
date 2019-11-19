"""This module defines Pool class"""
import math
import random
import config


POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """Pool class for our fish"""
    def __init__(self):
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self.fishes = []

    def get_size(self):
        """Return pool size"""
        return self._width, self._height

    def fill(self, fish_type, number: int):
        """Fills the pool"""
        self.fishes += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        val = '+' + '-' * self._width + '+\n'
        p_val = [[' ']*self._width for _ in range(self._height)]
        for fish in self.fishes:
            p_val[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in p_val:
            val += '|' + ''.join(row) + '|\n'
        val += '+' + '-'*self._width + '+\n'
        return val

    def tick(self):
        """The fish cycle in the pool"""
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

    def get_nearest_victim(self, axis_x, axis_y):
        """Find nearest dish..em, sorry, i wanted to say 'fish'"""
        nearest_victims = [fish.get_pos() for fish in self.fishes
                           if fish.is_victim]
        if not nearest_victims:
            return (0, 0)
        return tuple(min(
            nearest_victims,
            key=lambda f: math.hypot(f[0] - axis_x, f[1] - axis_y)))

    def get_victim(self, pos):
        """Get victim)"""
        return [fish for fish in self.fishes
                if fish.get_pos() == pos and fish.is_victim()]

    def kill(self, victim):
        """Death is just the beginning"""
        self.fishes.remove(victim)
