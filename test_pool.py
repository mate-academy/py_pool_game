"""This is docstring"""
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """This is class docstring"""
    def setUp(self) -> None:
        self.pool = pool.Pool()

    def test_pool(self):
        """This is function docstring"""
        self.assertEqual(self.pool.get_size(),
                         (20, 20), "Pool size doesn't equal 10x10")

    def test_fill_predators(self):
        """This is function docstring"""
        predators_quantity = 3
        lenght = len(self.pool.fishes)
        self.pool.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.pool.fishes), lenght + predators_quantity)

    @unittest.mock.patch("random.randint")
    def test_fill_predators_random(self, m_value):
        """This is function docstring"""
        m_value.side_effect = 0, 1
        self.pool.fill(fishes.Predator, 1)
        self.assertEqual(self.pool.fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch("random.randint")
    def test_nearest_victim(self, m_value):
        """This is function docstring"""
        m_value.side_effect = 1, 1, 5, 5, 9, 0
        self.pool.fill(fishes.Victim, 3)
        self.assertEqual(self.pool.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.pool.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch("random.randint")
    def test_get_victim(self, m_value):
        """This is function docstring"""
        m_value.side_effect = 1, 1
        self.pool.fill(fishes.Victim, 1)
        self.assertEqual(self.pool.get_victim([1, 1]), [self.pool.fishes[0]])

    def tearDown(self) -> None:
        pass


class TestFish(unittest.TestCase):
    """This is function docstring"""
    def test_fish_is_in_bounds1(self):
        """This is function docstring"""
        c_value = fishes.Fish(-1, -1)
        c_value.place_in_bounds(pool.Pool())
        self.assertEqual(c_value.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """This is function docstring"""
        c_value = fishes.Fish(10, 10)
        c_value.place_in_bounds(pool.Pool())
        self.assertEqual(c_value.get_pos(), [10, 10])


class TestPredator(unittest.TestCase):
    """This is class docstring"""
    def test_predator(self):
        """This is function docstring"""
        predator = fishes.Predator(2, 3)
        self.assertEqual(repr(predator), "P")

    def test_predator_pos(self):
        """This is function docstring"""
        predator = fishes.Predator(2, 3)
        self.assertEqual(predator.get_pos(), [2, 3])

    @unittest.mock.patch("random.randint")
    def test_predator_move(self, m_value):
        """This is function docstring"""
        p_value = pool.Pool()
        m_value.side_effect = 1, 1, 5, 5
        p_value.fill(fishes.Victim, 1)
        p_value.fill(fishes.Predator, 1)
        p_value.fishes[1].move(p_value)
        self.assertEqual(p_value.fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch("random.randint")
    def test_predator_eating(self, m_value):
        """This is function docstring"""
        p_value = pool.Pool()
        m_value.side_effect = 1, 1, 1, 1
        p_value.fill(fishes.Predator, 1)
        p_value.fill(fishes.Victim, 1)
        p_value.fishes[0].eat(p_value)
        self.assertEqual(len(p_value.fishes), 1)


class TestVictim(unittest.TestCase):
    """This is class docstring"""
    def test_victim(self):
        """This is function docstring"""
        c_value = fishes.Victim(2, 3)
        self.assertEqual(repr(c_value), "V")

    def test_victim_pos(self):
        """This is function docstring"""
        c_value = fishes.Victim(2, 3)
        self.assertEqual(c_value.get_pos(), [2, 3])

    @unittest.mock.patch("random.randint")
    def test_victim_correct_move(self, m_value):
        """This is function docstring"""
        c_value = fishes.Victim(2, 3)
        m_value.side_effect = 1, 1
        c_value.move(pool.Pool())
        self.assertEqual(c_value.get_pos(), [3, 4])
