"""Docstring"""
import unittest
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """Docstring"""
    def setUp(self) -> None:
        self.pol = pool.Pool()

    def test_pool(self):
        """Docstring"""
        self.assertEqual(self.pol.get_size(), (20, 20),
                         "Pool size doesn't equal 20x20")

    def test_fill_predators(self):
        """Docstring"""
        predators_quantity = 3
        len_fish = len(self.pol.fishes)
        self.pol.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.pol.fishes), len_fish + predators_quantity)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, make):
        """Docstring"""
        make.side_effect = 0, 1
        self.pol.fill(fishes.Predator, 1)
        self.assertEqual(self.pol.fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, make):
        """Docstring"""
        make.side_effect = 1, 1, 5, 5, 9, 0
        self.pol.fill(fishes.Victim, 3)
        self.assertEqual(self.pol.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.pol.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, make):
        """Docstring"""
        make.side_effect = 1, 1
        self.pol.fill(fishes.Victim, 1)
        self.assertEqual(self.pol.get_victim([1, 1]), [self.pol.fishes[0]])

    def tearDown(self) -> None:
        pass


class TestFish(unittest.TestCase):
    """Docstring"""
    def test_fish_is_in_bounds1(self):
        """Docstring"""
        vctm = fishes.Fish(-1, -1)
        vctm.place_in_bounds(pool.Pool())
        self.assertEqual(vctm.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """Docstring"""
        vctm = fishes.Fish(20, 20)
        vctm.place_in_bounds(pool.Pool())
        self.assertEqual(vctm.get_pos(), [19, 19])


class TestPredator(unittest.TestCase):
    """Docstring"""
    def test_predator(self):
        """Docstring"""
        pred = fishes.Predator(2, 3)
        self.assertEqual(repr(pred), 'P')

    def test_predator_pos(self):
        """Docstring"""
        pred = fishes.Predator(2, 3)
        self.assertEqual(pred.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, make):
        """Docstring"""
        pll = pool.Pool()
        make.side_effect = 1, 1, 5, 5
        pll.fill(fishes.Victim, 1)
        pll.fill(fishes.Predator, 1)
        pll.fishes[1].move(pll)
        self.assertEqual(pll.fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, make):
        """Docstring"""
        pll = pool.Pool()
        make.side_effect = 1, 1, 1, 1
        pll.fill(fishes.Predator, 1)
        pll.fill(fishes.Victim, 1)
        pll.fishes[0].eat(pll)
        self.assertEqual(len(pll.fishes), 1)


class TestVictim(unittest.TestCase):
    """Docstring"""
    def test_victim(self):
        """Docstring"""
        vctm = fishes.Victim(2, 3)
        self.assertEqual(repr(vctm), 'V')

    def test_victim_pos(self):
        """Docstring"""
        vctm = fishes.Victim(2, 3)
        self.assertEqual(vctm.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, make):
        """Docstring"""
        vctm = fishes.Victim(2, 3)
        make.side_effect = 1, 1
        vctm.move(pool.Pool())
        self.assertEqual(vctm.get_pos(), [3, 4])
