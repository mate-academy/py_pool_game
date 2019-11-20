"""
  Z name main
  Nain jjk.
"""
import random
import math
import config

POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """
      Z name main
      Nain jjk.
      """
    def __init__(self):
        """
          Z name main
          Nain jjk.
          """
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self._fishes = []

    def get_fishes(self):
        """function docstring"""
        return self._fishes

    def get_size(self):
        """
          Z name main
          Nain jjk.
          """
        return self._width, self._height

    def fill(self, fish_type, number: int):
        """
          Z name main
          Nain jjk.
          """
        self._fishes += [fish_type(random.randint(0, self._width - 1),
                                   random.randint(0, self._height - 1))
                         for _ in range(number)]

    def __str__(self):
        """
          Z name main
          Nain jjk.
          """
        s_ss = '+' + '-' * self._width + '+\n'
        p_pp = [[' '] * self._width for _ in range(self._height)]
        for fish in self._fishes:
            p_pp[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in p_pp:
            s_ss += '|' + ''.join(row) + '|\n'
        s_ss += '+' + '-' * self._width + '+\n'
        return s_ss

    def tick(self):
        """
          Z name main
          Nain jjk.
          """
        for fish in self._fishes:
            fish.move(self)
            fish.eat(self)

        for fish in self._fishes.copy():
            if not fish.is_alive():
                self.kill(fish)
        # else:
            # for fish in self._fishes.copy():
            #    fish.born(self)

    def get_nearest_victim(self, x_xx, y_yy):
        """
          Z name main
          Nain jjk.
          """
        nearest_victims = [fish.get_pos()
                           for fish in self._fishes if fish.is_victim()]

        if not nearest_victims:
            return (0, 0)
        return tuple(min(nearest_victims, key=lambda f: math.hypot(f[0] - x_xx,
                                                                   f[1] - y_yy)
                         ))

    def get_victim(self, pos):
        """
          Z name main
          Nain jjk.
          """
        return [fish for fish in self._fishes
                if fish.get_pos() == pos and fish.is_victim()]

    def kill(self, victim):
        """
          Z name main
          Nain jjk.
          """
        self._fishes.remove(victim)
