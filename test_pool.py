"""test project"""


import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """test pool object"""
    def setUp(self) -> None:
        """ init"""
        self.poo = pool.Pool()

    def test_pool(self):
        """test size"""
        self.assertEqual(self.poo.get_size(),
                         (20, 20), "Pool size doesn't equal 20x20")

    def test_fill_predators(self):
        """test fill predators"""
        predators_quantity = 3
        lngth = len(self.poo.fishes)
        self.poo.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.poo.fishes), lngth + predators_quantity)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, moo):
        """test fill random predators"""
        moo.side_effect = 0, 1
        self.poo.fill(fishes.Predator, 1)
        self.assertEqual(self.poo.fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, moo):
        """test nearest victim"""
        moo.side_effect = 1, 1, 5, 5, 9, 0
        self.poo.fill(fishes.Victim, 3)
        self.assertEqual(self.poo.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.poo.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, moo):
        """test get victim"""
        moo.side_effect = 1, 1
        self.poo.fill(fishes.Victim, 1)
        self.assertEqual(self.poo.get_victim([1, 1]), [self.poo.fishes[0]])


class TestFish(unittest.TestCase):
    """test object fish"""
    def test_fish_is_in_bounds1(self):
        """test fish in boundls"""
        vctm = fishes.Fish(-1, -1)
        vctm.place_in_bounds(pool.Pool())
        self.assertEqual(vctm.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """second"""
        vctm = fishes.Fish(20, 20)
        vctm.place_in_bounds(pool.Pool())
        self.assertEqual(vctm.get_pos(), [19, 19])


class TestPredator(unittest.TestCase):
    """test object predator"""
    def test_predator(self):
        """init predator"""
        pred = fishes.Predator(2, 3)
        self.assertEqual(repr(pred), 'P')

    def test_predator_pos(self):
        """test predator possition"""
        pred = fishes.Predator(2, 3)
        self.assertEqual(pred.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, moo):
        """test move predat"""
        poo = pool.Pool()
        moo.side_effect = 1, 1, 5, 5
        poo.fill(fishes.Victim, 1)
        poo.fill(fishes.Predator, 1)
        poo.fishes[1].move(poo)
        self.assertEqual(poo.fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, moo):
        """test predator eat"""
        poo = pool.Pool()
        moo.side_effect = 1, 1, 1, 1
        poo.fill(fishes.Predator, 1)
        poo.fill(fishes.Victim, 1)
        poo.fishes[0].eat(poo)
        self.assertEqual(len(poo.fishes), 1)


class TestVictim(unittest.TestCase):
    """test object vittims"""
    def test_victim(self):
        """test victim init"""
        vctm = fishes.Victim(2, 3)
        self.assertEqual(repr(vctm), 'V')

    def test_victim_pos(self):
        """test victim pos"""
        vctm = fishes.Victim(2, 3)
        self.assertEqual(vctm.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, moo):
        """test victim corre"""
        vctm = fishes.Victim(2, 3)
        moo.side_effect = 1, 1
        vctm.move(pool.Pool())
        self.assertEqual(vctm.get_pos(), [3, 4])
