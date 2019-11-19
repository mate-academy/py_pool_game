"""
  Z name main
  Nain jjk.
"""
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """
      Z name main
      Nain jjk.
      """
    def setUp(self) -> None:
        """
          Z name main
          Nain jjk.
          """
        self.p = pool.Pool()

    def test_pool(self):
        """
          Z name main
          Nain jjk.
          """
        self.assertEqual(self.p.get_size(), (20, 20),
                         "Pool size doesn't equal 20x20")

    def test_fill_predators(self):
        """
          Z name main
          Nain jjk.
          """
        PREDATORS_QUANTITY = 3
        Length = len(self.p._fishes)
        self.p.fill(fishes.Predator, PREDATORS_QUANTITY)
        self.assertEqual(len(self.p._fishes), Length + PREDATORS_QUANTITY)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, m):
        """
          Z name main
          Nain jjk.
          """
        m.side_effect = 0, 1
        self.p.fill(fishes.Predator, 1)
        self.assertEqual(self.p._fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, m):
        """
          Z name main
          Nain jjk.
          """
        m.side_effect = 1, 1, 5, 5, 9, 0
        self.p.fill(fishes.Victim, 3)
        self.assertEqual(self.p.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.p.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, m):
        """
          Z name main
          Nain jjk.
          """
        m.side_effect = 1, 1
        self.p.fill(fishes.Victim, 1)
        self.assertEqual(self.p.get_victim([1, 1]), [self.p._fishes[0]])

    def tearDown(self) -> None:
        """
          Z name main
          Nain jjk.
          """
        pass


class TestFish(unittest.TestCase):
    """
      Z name main
      Nain jjk.
      """
    def test_fish_is_in_bounds1(self):
        """
          Z name main
          Nain jjk.
          """
        vc = fishes.Fish(-1, -1)
        vc.place_in_bounds(pool.Pool())
        self.assertEqual(vc.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """
          Z name main
          Nain jjk.
          """
        vc = fishes.Fish(20, 20)
        vc.place_in_bounds(pool.Pool())
        self.assertEqual(vc.get_pos(), [19, 19])


class TestPredator(unittest.TestCase):
    """
      Z name main
      Nain jjk.
      """
    def test_predator(self):
        """
          Z name main
          Nain jjk.
          """
        pr = fishes.Predator(2, 3)
        self.assertEqual(repr(pr), 'P')

    def test_predator_pos(self):
        """
          Z name main
          Nain jjk.
          """
        pr = fishes.Predator(2, 3)
        self.assertEqual(pr.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, m):
        """
          Z name main
          Nain jjk.
          """
        p = pool.Pool()
        m.side_effect = 1, 1, 5, 5
        p.fill(fishes.Victim, 1)
        p.fill(fishes.Predator, 1)
        p._fishes[1].move(p)
        self.assertEqual(p._fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, m):
        """
          Z name main
          Nain jjk.
          """
        p = pool.Pool()
        m.side_effect = 1, 1, 1, 1
        p.fill(fishes.Predator, 1)
        p.fill(fishes.Victim, 1)
        p._fishes[0].eat(p)
        self.assertEqual(len(p._fishes), 1)


class TestVictim(unittest.TestCase):
    """
      Z name main
      Nain jjk.
      """
    def test_victim(self):
        """
          Z name main
          Nain jjk.
          """
        vc = fishes.Victim(2, 3)
        self.assertEqual(repr(vc), 'V')

    def test_victim_pos(self):
        """
          Z name main
          Nain jjk.
          """
        vc = fishes.Victim(2, 3)
        self.assertEqual(vc.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, m):
        """
          Z name main
          Nain jjk.
          """
        vc = fishes.Victim(2, 3)
        m.side_effect = 1, 1
        vc.move(pool.Pool())
        self.assertEqual(vc.get_pos(), [3, 4])
