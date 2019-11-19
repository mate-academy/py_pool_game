"""
docstring
"""

import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """
    test class
    """

    def setUp(self) -> None:
        """

        :return:
        """
        self.pas = pool.Pool()

    def test_pool(self):
        """

        :return:
        """
        self.assertEqual(self.pas.get_size(),
                         (20, 20), "Pool size doesn't equal 20x20")

    def test_fill_predators(self):
        """

        :return:
        """
        predators_quantity = 3
        length = len(self.pas.get_fishes())
        self.pas.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.pas.get_fishes()),
                         length + predators_quantity)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, mcp):
        """

        :param mcp:
        :return:
        """
        mcp.side_effect = 0, 1
        self.pas.fill(fishes.Predator, 1)
        self.assertEqual(self.pas.get_fishes()[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, mcp):
        """

        :param mcp:
        :return:
        """
        mcp.side_effect = 1, 1, 5, 5, 9, 0
        self.pas.fill(fishes.Victim, 3)
        self.assertEqual(self.pas.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.pas.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, mcp):
        """

        :param mcp:
        :return:
        """
        mcp.side_effect = 1, 1
        self.pas.fill(fishes.Victim, 1)
        self.assertEqual(self.pas.get_victim([1, 1]),
                         [self.pas.get_fishes()[0]])

    def tearDown(self) -> None:
        """

        :return:
        """


class TestFish(unittest.TestCase):
    """
    Fish tests
    """

    def test_fish_is_in_bounds1(self):
        """

        :return:
        """
        vctm = fishes.Fish(-1, -1)
        vctm.place_in_bounds(pool.Pool())
        self.assertEqual(vctm.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """

        :return:
        """
        vctm = fishes.Fish(20, 20)
        vctm.place_in_bounds(pool.Pool())
        self.assertEqual(vctm.get_pos(), [19, 19])


class TestPredator(unittest.TestCase):
    """
    Predator tests
    """

    def test_predator(self):
        """

        :return:
        """
        prdtr = fishes.Predator(2, 3)
        self.assertEqual(repr(prdtr), 'P')

    def test_predator_pos(self):
        """

        :return:
        """
        prdtr = fishes.Predator(2, 3)
        self.assertEqual(prdtr.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, mcp):
        """

        :param mcp:
        :return:
        """
        pas = pool.Pool()
        mcp.side_effect = 1, 1, 5, 5
        pas.fill(fishes.Victim, 1)
        pas.fill(fishes.Predator, 1)
        pas.get_fishes()[1].move(pas)
        self.assertEqual(pas.get_fishes()[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, mcp):
        """

        :param mcp:
        :return:
        """
        pas = pool.Pool()
        mcp.side_effect = 1, 1, 1, 1
        pas.fill(fishes.Predator, 1)
        pas.fill(fishes.Victim, 1)
        pas.get_fishes()[0].eat(pas)
        self.assertEqual(len(pas.get_fishes()), 1)


class TestVictim(unittest.TestCase):
    """
    Victim tests
    """

    def test_victim(self):
        """

        :return:
        """
        vctm = fishes.Victim(2, 3)
        self.assertEqual(repr(vctm), 'V')

    def test_victim_pos(self):
        """

        :return:
        """
        vctm = fishes.Victim(2, 3)
        self.assertEqual(vctm.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, mcp):
        """

        :param mcp:
        :return:
        """
        vctm = fishes.Victim(2, 3)
        mcp.side_effect = 1, 1
        vctm.move(pool.Pool())
        self.assertEqual(vctm.get_pos(), [3, 4])
