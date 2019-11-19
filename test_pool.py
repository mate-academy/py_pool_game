"""Module test_pool"""
import unittest
import unittest.mock
import pool
import fishes

P_W = pool.POOL_WIDTH
P_H = pool.POOL_HEIGHT


class TestPool(unittest.TestCase):
    """TestPool class"""
    def setUp(self) -> None:
        """

        :return:
        """
        self.pol = pool.Pool()

    def test_pool(self):
        """

        :return:
        """
        self.assertEqual(self.pol.get_size(), (P_W, P_H),
                         "Pool size doesn't equal 10x10")

    def test_fill_predators(self):
        """

        :return:
        """
        num_of_predators = 3
        lan = len(self.pol.fish_in_pool)
        self.pol.fill(fishes.Predator, num_of_predators)
        self.assertEqual(len(self.pol.fish_in_pool), lan + num_of_predators)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, mel):
        """

        :param mel:
        :return:
        """
        mel.side_effect = 0, 1
        self.pol.fill(fishes.Predator, 1)
        self.assertEqual(self.pol.fish_in_pool[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, mel):
        """

        :param mel:
        :return:
        """
        mel.side_effect = 1, 1, 5, 5, 9, 0
        self.pol.fill(fishes.Victim, 3)
        self.assertEqual(self.pol.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.pol.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, mol):
        """

        :param mol:
        :return:
        """
        mol.side_effect = 1, 1
        self.pol.fill(fishes.Victim, 1)
        self.assertEqual(self.pol.get_victim([1, 1]),
                         [self.pol.fish_in_pool[0]])

    def tearDown(self) -> None:
        """

        :return:
        """


class TestFish(unittest.TestCase):
    """TestFish class"""
    def test_fish_is_in_bounds1(self):
        """

        :return:
        """
        corn_pos = fishes.Fish(-1, -1)
        corn_pos.place_in_bounds(pool.Pool())
        self.assertEqual(corn_pos.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """

        :return:
        """
        corn_pos = fishes.Fish(P_W, P_H)
        corn_pos.place_in_bounds(pool.Pool())
        self.assertEqual(corn_pos.get_pos(), [P_W - 1, P_H - 1])


class TestPredator(unittest.TestCase):
    """TestPredator class"""
    def test_predator(self):
        """

        :return:
        """
        pred = fishes.Predator(2, 3)
        self.assertEqual(repr(pred), 'P')

    def test_predator_pos(self):
        """

        :return:
        """
        pred = fishes.Predator(2, 3)
        self.assertEqual(pred.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, mel):
        """

        :param mel:
        :return:
        """
        pol = pool.Pool()
        mel.side_effect = 1, 1, 5, 5
        pol.fill(fishes.Victim, 1)
        pol.fill(fishes.Predator, 1)
        pol.fish_in_pool[1].move(pol)
        self.assertEqual(pol.fish_in_pool[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, mel):
        """

        :param mel:
        :return:
        """
        pol = pool.Pool()
        mel.side_effect = 1, 1, 1, 1
        pol.fill(fishes.Predator, 1)
        pol.fill(fishes.Victim, 1)
        pol.fish_in_pool[0].eat(pol)
        self.assertEqual(len(pol.fish_in_pool), 1)


class TestVictim(unittest.TestCase):
    """TestVictim class"""
    def test_victim(self):
        """

        :return:
        """
        vict = fishes.Victim(2, 3)
        self.assertEqual(repr(vict), 'V')

    def test_victim_pos(self):
        """

        :return:
        """
        vict = fishes.Victim(2, 3)
        self.assertEqual(vict.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, mel):
        """

        :param mel:
        :return:
        """
        vict = fishes.Victim(2, 3)
        mel.side_effect = 1, 1
        vict.move(pool.Pool())
        self.assertEqual(vict.get_pos(), [3, 4])
