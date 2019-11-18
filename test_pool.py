"""DOCSTRING"""
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """DOCSTRING"""
    def setUp(self) -> None:
        self.pool123 = pool.Pool()

    def test_pool(self):
        """DOCSTRING"""
        self.assertEqual(self.pool123.get_size(), (20, 20),
                         "Pool size doesn't equal 20x20")

    def test_fill_predators(self):
        """DOCSTRING"""
        predators_qual = 3
        lenght = len(self.pool123.fishes)
        self.pool123.fill(fishes.Predator, predators_qual)
        self.assertEqual(len(self.pool123.fishes), lenght + predators_qual)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, make):
        """DOCSTRING"""
        make.side_effect = 0, 1
        self.pool123.fill(fishes.Predator, 1)
        self.assertEqual(self.pool123.fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, maker):
        """DOCSTRING"""
        maker.side_effect = 1, 1, 5, 5, 9, 0
        self.pool123.fill(fishes.Victim, 3)
        self.assertEqual(self.pool123.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.pool123.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, make):
        """DOCSTRING"""
        make.side_effect = 1, 1
        self.pool123.fill(fishes.Victim, 1)
        self.assertEqual(self.pool123.get_victim([1, 1]),
                         [self.pool123.fishes[0]])

    def tearDown(self) -> None:
        pass


class TestFish(unittest.TestCase):
    """DOCSTRING"""
    def test_fish_is_in_bounds1(self):
        """DOCSTRING"""
        vconat = fishes.Fish(-1, -1)
        vconat.place_in_bounds(pool.Pool())
        self.assertEqual(vconat.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """DOCSTRING"""
        vconat = fishes.Fish(20, 20)
        vconat.place_in_bounds(pool.Pool())
        self.assertEqual(vconat.get_pos(), [19, 19])


class TestPredator(unittest.TestCase):
    """DOCSTRING"""
    def test_predator(self):
        """DOCSTRING"""
        prokal = fishes.Predator(2, 3)
        self.assertEqual(repr(prokal), 'P')

    def test_predator_pos(self):
        """DOCSTRING"""
        prokal = fishes.Predator(2, 3)
        self.assertEqual(prokal.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, make):
        """DOCSTRING"""
        porka = pool.Pool()
        make.side_effect = 1, 1, 5, 5
        porka.fill(fishes.Victim, 1)
        porka.fill(fishes.Predator, 1)
        porka.fishes[1].move(porka)
        self.assertEqual(porka.fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, make):
        """DOCSTRING"""
        porka = pool.Pool()
        make.side_effect = 1, 1, 1, 1
        porka.fill(fishes.Predator, 1)
        porka.fill(fishes.Victim, 1)
        porka.fishes[0].eat(porka)
        self.assertEqual(len(porka.fishes), 1)


class TestVictim(unittest.TestCase):
    """DOCSTRING"""
    def test_victim(self):
        """DOCSTRING"""
        vcolka = fishes.Victim(2, 3)
        self.assertEqual(repr(vcolka), 'V')

    def test_victim_pos(self):
        """DOCSTRING"""
        vcolka = fishes.Victim(2, 3)
        self.assertEqual(vcolka.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, make):
        """DOCSTRING"""
        vcontra = fishes.Victim(2, 3)
        make.side_effect = 1, 1
        vcontra.move(pool.Pool())
        self.assertEqual(vcontra.get_pos(), [3, 4])
