"""Pool module description."""
import random
import math
import config


POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """Pool class."""
    def __init__(self):
        """Pool constructor."""
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self.fishes = []

    def get_size(self):
        """Get pool's size."""
        return self._width, self._height

    def fill(self, fish_type, number: int):
        """Fill a pool with fish."""
        self.fishes += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        """don't know what it does."""
        some_string = '+' + '-'*self._width + '+\n'
        place = [[' ']*self._width for _ in range(self._height)]
        for fish in self.fishes:
            place[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in place:
            some_string += '|' + ''.join(row) + '|\n'
        some_string += '+' + '-'*self._width + '+\n'
        return some_string

    def tick(self):
        """Tick a fish."""
        for fish in self.fishes:
            fish.move(self)
            fish.eat(self)

        for fish in self.fishes.copy():
            if not fish.is_alive():
                self.kill(fish)
        for fish in self.fishes.copy():
            fish.born(self)

    def get_nearest_victim(self, x_position, y_position):
        """Define a victim."""
        nearest_victims = [fish.get_pos()
                           for fish in self.fishes if fish.is_victim()]
        if not nearest_victims:
            return 0, 0
        return tuple(min(nearest_victims,
                         key=lambda f: math.hypot(f[0] - x_position,
                                                  f[1] - y_position)))

    def get_victim(self, pos):
        """Catch a victim."""
        return [fish for fish in self.fishes
                if fish.get_pos() == pos and fish.is_victim()]

    def kill(self, victim):
        """remove a fish-victim from list."""
        self.fishes.remove(victim)
