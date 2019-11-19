"""
  Z name main
  Nain jjk.
"""
import json
import random

import pool

X, Y = 0, 1


class Fish:
    """
      Z name main
      Nain jjk.
      """
    def __init__(self, x, y):
        """
          Z name main
          Nain jjk.
          """
        self._pos = [x, y]
        self._life_counter = 10
        self._born_rate = 0
        self._born_num = 0
        self._is_not_hungry = 0

    def get_pos(self):
        """
          Z name main
          Nain jjk.
          """
        return self._pos

    def move(self, p_ppp: pool.Pool) -> tuple:
        """
          Z name main
          Nain jjk.
          """
        self._life_counter -= 1
        self._move(p_ppp)
        p_ppp1 = [p_ppp]
        self.place_in_bounds(p_ppp1)
        return tuple(p_ppp1)

    def is_alive(self):
        """
          Z name main
          Nain jjk.
          """
        return self._life_counter > 0

    def _move(self, p_ppp: pool.Pool):
        """
          Z name main
          Nain jjk.
          """
#        pass
    @staticmethod
    def is_victim():
        """
          Z name main
          Nain jjk.
          """
        return False

    def place_in_bounds(self, p_ppp: list):
        """
          Z name main
          Nain jjk.
          """
        try:
            self._pos[X] = min(max(self._pos[X], 0), p_ppp.get_size()[X] - 1)
            self._pos[Y] = min(max(self._pos[Y], 0), p_ppp.get_size()[Y] - 1)
        except ValueError:
            print("Oooops!")

    def eat(self, p_ppp: pool.Pool):
        """
          Z name main
          Nain jjk.
          """
     #   pass

    def born(self, p_ppp: pool.Pool):
        """
          Z name main
          Nain jjk.
          """
        if random.randint(1, 10) < self._born_rate:
            p_ppp.fill(self.__class__, self._born_num)


class Predator(Fish):
    """
      Z name main
      Nain jjk.
      """
    with open("predator.json", 'rt') as f:
        state = json.load(f)

    with open('predator.json', 'rt') as f:
        predator_state = json.load(f)

    def __init__(self, x, y):
        """
          Z name main
          Nain jjk.
          """
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, p_ppp: pool.Pool = None):
        """
          Z name main
          Nain jjk.
          """
        self._is_not_hungry -= 1
        victim = p_ppp.get_nearest_victim(*self._pos)
        self._pos[X] += 2 if victim[X] > self._pos[X] else -2
        self._pos[Y] += 2 if victim[Y] > self._pos[Y] else -2

    def eat(self, p_ppp: pool.Pool) -> int:
        """
        Fgfghs ms
        """
        victims = p_ppp.get_victim(self.get_pos())
        if victims:
            self._is_not_hungry += 3
            for victim in victims:
                p_ppp.kill(victim)

    def __repr__(self):
        """
          Z name main
          Nain jjk.
          """
        return "P"

    def is_alive(self):
        """
          Z name main
          Nain jjk.
          """
        return super().is_alive() and self._is_not_hungry > 0


class Victim(Fish):
    """
      Z name main
      Nain jjk.
      """
    with open("victim.json", 'rt') as f:
        state = json.load(f)

    def __init__(self, x, y):
        """
          Z name main
          Nain jjk.
          """
        super().__init__(x, y)
        self.__dict__.update(self.state)

    def _move(self, p_ppp: pool.Pool):
        """
          Z name main
          Nain jjk.
          """
        self._pos[X] += random.randint(-1, 1)
        self._pos[Y] += random.randint(-1, 1)

    def __repr__(self):
        """
          Z name main
          Nain jjk.
          """
        return "V"

    def is_victim(self):
        """
          Z name main
          Nain jjk.
          """
        return True


class Pike(Predator):
    """
      Z name main
      Nain jjk.
      """
    def __init__(self):
        """
          Z name main
          Nain jjk.
          """
        self._life_counter = 10
        self._born_rate = 3
        self._born_num = 2
        super(Pike, self).__init__(self)
