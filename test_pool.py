"""
module docstring
"""
import unittest.mock

import fishes
import pool


class TestPool(unittest.TestCase):
    """tests for Pool class"""

    def setUp(self) -> None:
        """

        :return:
        """
        self.basin = pool.Pool()

    def test_pool(self):
        """

        :return:
        """
        self.assertEqual(self.basin.get_size(), (20, 20),
                         "Pool size doesn't equal 20x20")

    def test_fill_predators(self):
        """

        :return:
        """
        predators_qty = 3
        length = len(self.basin.get_fishes())
        self.basin.fill(fishes.Predator, predators_qty)
        self.assertEqual(len(self.basin.get_fishes()), length + predators_qty)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, mck):
        """

        :param mck:
        :return:
        """
        mck.side_effect = 0, 1
        self.basin.fill(fishes.Predator, 1)
        self.assertEqual(self.basin.get_fishes()[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, mck):
        """

        :param mck:
        :return:
        """
        mck.side_effect = 1, 1, 5, 5, 9, 0
        self.basin.fill(fishes.Victim, 3)
        self.assertEqual(self.basin.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.basin.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, mck):
        """

        :param mck:
        :return:
        """
        mck.side_effect = 1, 1
        self.basin.fill(fishes.Victim, 1)
        self.assertEqual(
            self.basin.get_victim([1, 1]), [self.basin.get_fishes()[0]]
        )

    def tearDown(self) -> None:
        """

        :return:
        """


class TestFish(unittest.TestCase):
    """tests for Fish class"""

    def test_fish_is_in_bounds1(self):
        """

        :return:
        """
        victim = fishes.Fish(-1, -1)
        victim.place_in_bounds(pool.Pool())
        self.assertEqual(victim.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """

        :return:
        """
        victim = fishes.Fish(20, 20)
        victim.place_in_bounds(pool.Pool())
        self.assertEqual(victim.get_pos(), [19, 19])


class TestPredator(unittest.TestCase):
    """tests for Predator class"""

    def test_predator(self):
        """

        :return:
        """
        predator = fishes.Predator(2, 3)
        self.assertEqual(repr(predator), 'P')

    def test_predator_pos(self):
        """

        :return:
        """
        predator = fishes.Predator(2, 3)
        self.assertEqual(predator.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, mck):
        """

        :param mck:
        :return:
        """
        basin = pool.Pool()
        mck.side_effect = 1, 1, 5, 5
        basin.fill(fishes.Victim, 1)
        basin.fill(fishes.Predator, 1)
        basin.get_fishes()[1].move(basin)
        self.assertEqual(basin.get_fishes()[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, mck):
        """

        :param mck:
        :return:
        """
        basin = pool.Pool()
        mck.side_effect = 1, 1, 1, 1
        basin.fill(fishes.Predator, 1)
        basin.fill(fishes.Victim, 1)
        basin.get_fishes()[0].eat(basin)
        self.assertEqual(len(basin.get_fishes()), 1)


class TestVictim(unittest.TestCase):
    """tests for Victim class"""

    def test_victim(self):
        """

        :return:
        """
        victim = fishes.Victim(2, 3)
        self.assertEqual(repr(victim), 'V')

    def test_victim_pos(self):
        """

        :return:
        """
        victim = fishes.Victim(2, 3)
        self.assertEqual(victim.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, mck):
        """

        :param mck:
        :return:
        """
        victim = fishes.Victim(2, 3)
        mck.side_effect = 1, 1
        victim.move(pool.Pool())
        self.assertEqual(victim.get_pos(), [3, 4])
