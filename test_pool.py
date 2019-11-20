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
        self.p_ppp = pool.Pool()

    def test_pool(self):
        """
          Z name main
          Nain jjk.
          """
        self.assertEqual(self.p_ppp.get_size(), (20, 20),
                         "Pool size doesn't equal 20x20")

    def test_fill_predators(self):
        """
          Z name main
          Nain jjk.
          """
        predators_quantity = 3
        length = len(self.p_ppp.get_fishes())
        self.p_ppp.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.p_ppp.get_fishes()),
                         length + predators_quantity)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, m_mmm):
        """
          Z name main
          Nain jjk.
          """
        m_mmm.side_effect = 0, 1
        self.p_ppp.fill(fishes.Predator, 1)
        self.assertEqual(self.p_ppp.get_fishes()[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, m_mmm):
        """
          Z name main
          Nain jjk.
          """
        m_mmm.side_effect = 1, 1, 5, 5, 9, 0
        self.p_ppp.fill(fishes.Victim, 3)
        self.assertEqual(self.p_ppp.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.p_ppp.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, m_mmm):
        """
          Z name main
          Nain jjk.
          """
        m_mmm.side_effect = 1, 1
        self.p_ppp.fill(fishes.Victim, 1)
        self.assertEqual(self.p_ppp.get_victim([1, 1]),
                         [self.p_ppp.get_fishes()[0]])

    # def tearDown(self) -> None:
        # """
        # Z name main
        # Nain jjk.
        # """
        # pass


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
        v_c = fishes.Fish(-1, -1)
        v_c.place_in_bounds(pool.Pool())
        self.assertEqual(v_c.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """
          Z name main
          Nain jjk.
          """
        v_c = fishes.Fish(20, 20)
        v_c.place_in_bounds(pool.Pool())
        self.assertEqual(v_c.get_pos(), [19, 19])


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
        p_r = fishes.Predator(2, 3)
        self.assertEqual(repr(p_r), 'P')

    def test_predator_pos(self):
        """
          Z name main
          Nain jjk.
          """
        p_r = fishes.Predator(2, 3)
        self.assertEqual(p_r.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, m_mmm):
        """
          Z name main
          Nain jjk.
          """
        p_ppp = pool.Pool()
        m_mmm.side_effect = 1, 1, 5, 5
        p_ppp.fill(fishes.Victim, 1)
        p_ppp.fill(fishes.Predator, 1)
        p_ppp.get_fishes()[1].move(p_ppp)
        self.assertEqual(p_ppp.get_fishes()[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, m_mmm):
        """
          Z name main
          Nain jjk.
          """
        p_ppp = pool.Pool()
        m_mmm.side_effect = 1, 1, 1, 1
        p_ppp.fill(fishes.Predator, 1)
        p_ppp.fill(fishes.Victim, 1)
        p_ppp.get_fishes()[0].eat(p_ppp)
        self.assertEqual(len(p_ppp.get_fishes()), 1)


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
        v_c = fishes.Victim(2, 3)
        self.assertEqual(repr(v_c), 'V')

    def test_victim_pos(self):
        """
          Z name main
          Nain jjk.
          """
        v_c = fishes.Victim(2, 3)
        self.assertEqual(v_c.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, m_mmm):
        """
          Z name main
          Nain jjk.
          """
        v_c = fishes.Victim(2, 3)
        m_mmm.side_effect = 1, 1
        v_c.move(pool.Pool())
        self.assertEqual(v_c.get_pos(), [3, 4])
