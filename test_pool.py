"""module docstrings"""
import unittest
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """class docstring"""
    def setUp(self) -> None:
        """docstring"""
        self.poo = pool.Pool()

    def test_pool(self):
        """docstring"""
        self.assertEqual(self.poo.get_size(), (10, 10),
                         "Pool size doesn't equal 10x10")

    def test_fill_predators(self):
        """docstring"""
        predators_quantity = 3
        leng = len(self.poo._fishes)
        self.poo.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.poo._fishes), leng + predators_quantity)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, mmm):
        """docstring"""
        mmm.side_effect = 0, 1
        self.poo.fill(fishes.Predator, 1)
        self.assertEqual(self.poo._fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, mmm):
        """docstring"""
        mmm.side_effect = 1, 1, 5, 5, 9, 0
        self.poo.fill(fishes.Victim, 3)
        self.assertEqual(self.poo.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.poo.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, mmm):
        """docstring"""
        mmm.side_effect = 1, 1
        self.poo.fill(fishes.Victim, 1)
        self.assertEqual(self.poo.get_victim([1, 1]), [self.poo._fishes[0]])


class TestFish(unittest.TestCase):
    """docstring"""
    def test_fish_is_in_bounds1(self):
        """docstring"""
        vcc = fishes.Fish(-1, -1)
        vcc.place_in_bounds(pool.Pool())
        self.assertEqual(vcc.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """docstring"""
        vcc = fishes.Fish(10, 10)
        vcc.place_in_bounds(pool.Pool())
        self.assertEqual(vcc.get_pos(), [9, 9])


class TestPredator(unittest.TestCase):
    """docstring"""
    def test_predator(self):
        """docstring"""
        pre = fishes.Predator(2, 3)
        self.assertEqual(repr(pre), 'P')

    def test_predator_pos(self):
        """docstring"""
        pre = fishes.Predator(2, 3)
        self.assertEqual(pre.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, mmm):
        """docstring"""
        poo = pool.Pool()
        mmm.side_effect = 1, 1, 5, 5
        poo.fill(fishes.Victim, 1)
        poo.fill(fishes.Predator, 1)
        poo._fishes[1].move(poo)
        self.assertEqual(poo._fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, mmm):
        """docstring"""
        poo = pool.Pool()
        mmm.side_effect = 1, 1, 1, 1
        poo.fill(fishes.Predator, 1)
        poo.fill(fishes.Victim, 1)
        poo._fishes[0].eat(poo)
        self.assertEqual(len(poo._fishes), 1)


class TestVictim(unittest.TestCase):
    """docstring"""
    def test_victim(self):
        """docstring"""
        vcc = fishes.Victim(2, 3)
        self.assertEqual(repr(vcc), 'V')

    def test_victim_pos(self):
        """docstring"""
        vcc = fishes.Victim(2, 3)
        self.assertEqual(vcc.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, mmm):
        """docstring """
        vcc = fishes.Victim(2, 3)
        mmm.side_effect = 1, 1
        vcc.move(pool.Pool())
        self.assertEqual(vcc.get_pos(), [3, 4])
