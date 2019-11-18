"""This is docstring"""
import random
import math
import config

POOL_WIDTH = int(config.CONFIG["Pool"]["Width"])
POOL_HEIGHT = int(config.CONFIG["Pool"]["Height"])


class Pool:
    """This is class docstring"""

    def __init__(self):
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self.fishes = []

    def get_size(self):
        """This is module docstring"""
        return self._width, self._height

    def fill(self, fish_type, number: int):
        """This is function docstring"""
        self.fishes += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        value = "+" + "-" * self._width + "+\n"
        p_value = [[" "] * self._width for _ in range(self._height)]
        for fish in self.fishes:
            p_value[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in p_value:
            value += "|" + "".join(row) + "|\n"
        value += "+" + "-" * self._width + "+\n"
        return value

    def tick(self):
        """This is function docstring"""
        for fish in self.fishes:
            fish.move(self)
            fish.eat(self)

        for fish in self.fishes.copy():
            if not fish.is_alive():
                self.kill(fish)
        for fish in self.fishes.copy():
            fish.born(self)

    def get_nearest_victim(self, x_val, y_val):
        """This is function docstring"""
        nearest_victims = [fish.get_pos() for fish in self.fishes
                           if fish.is_victim]
        if not nearest_victims:
            return (0, 0)
        return tuple(min(nearest_victims,
                         key=lambda f: math.hypot(f[0] - x_val, f[1] - y_val)))

    def get_victim(self, pos):
        """This is function docstring"""
        return [
            fish for fish in self.fishes if
            fish.get_pos() == pos and fish.is_victim
        ]

    def kill(self, victim):
        """This is function docstring"""
        self.fishes.remove(victim)
