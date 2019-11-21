"""
s
"""
import unittest
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """
    s
    """

    def setUp(self) -> None:
        """

        :return:
        """
        self.pool = pool.Pool()

    def test_pool(self):
        """

        :return:
        """
        self.assertEqual(
            self.pool.get_size(), (20, 20), "Pool size doesn't equal 10x10"
        )

    def test_fill_predators(self):
        """

        :return:
        """
        predators_quantity = 3
        length = len(self.pool.fishes)
        self.pool.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.pool.fishes), length + predators_quantity)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, mock):
        """

        :param mock:
        :return:
        """
        mock.side_effect = 0, 1
        self.pool.fill(fishes.Predator, 1)
        self.assertEqual(self.pool.fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, mock):
        """

        :param mock:
        :return:
        """
        mock.side_effect = 1, 1, 5, 5, 9, 0
        self.pool.fill(fishes.Victim, 3)
        self.assertEqual(self.pool.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.pool.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, mock):
        """

        :param mock:
        :return:
        """
        mock.side_effect = 1, 1
        self.pool.fill(fishes.Victim, 1)
        self.assertEqual(self.pool.get_victim([1, 1]), [self.pool.fishes[0]])


class TestFish(unittest.TestCase):
    """
    s
    """

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
    """
    s
    """

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
    def test_predator_move(self, mock):
        """

        :param mock:
        :return:
        """
        created_pool = pool.Pool()
        mock.side_effect = 1, 1, 5, 5
        created_pool.fill(fishes.Victim, 1)
        created_pool.fill(fishes.Predator, 1)
        created_pool.fishes[1].move(created_pool)
        self.assertEqual(created_pool.fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, mock):
        """

        :param mock:
        :return:
        """
        created_pool = pool.Pool()
        mock.side_effect = 1, 1, 1, 1
        created_pool.fill(fishes.Predator, 1)
        created_pool.fill(fishes.Victim, 1)
        created_pool.fishes[0].eat(created_pool)
        self.assertEqual(len(created_pool.fishes), 1)


class TestVictim(unittest.TestCase):
    """
    s
    """

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
    def test_victim_correct_move(self, mock):
        """

        :param mock:
        :return:
        """
        victim = fishes.Victim(2, 3)
        mock.side_effect = 1, 1
        victim.move(pool.Pool())
        self.assertEqual(victim.get_pos(), [3, 4])
