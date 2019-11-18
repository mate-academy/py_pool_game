import unittest
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    def setUp(self) -> None:
        self.p = pool.Pool()

    def test_pool(self):
        self.assertEqual(
            self.p.get_size(), (10, 10), "Pool size doesn't equal 10x10")

    def test_fill_predators(self):
        PREDATORS_QUANTITY = 3
        fises_len = len(self.p._fishes)
        self.p.fill(fishes.Predator, PREDATORS_QUANTITY)
        self.assertEqual(len(self.p._fishes), fises_len + PREDATORS_QUANTITY)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, m):
        m.side_effect = 0, 1
        self.p.fill(fishes.Predator, 1)
        self.assertEqual(self.p._fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, m):
        m.side_effect = 1, 1, 5, 5, 9, 0
        self.p.fill(fishes.Victim, 3)
        self.assertEqual(self.p.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.p.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, m):
        m.side_effect = 1, 1
        self.p.fill(fishes.Victim, 1)
        self.assertEqual(self.p.get_victim([1, 1]), [self.p._fishes[0]])

    def tearDown(self) -> None:
        pass


class TestFish(unittest.TestCase):
    def test_fish_is_in_bounds1(self):
        vc = fishes.Fish(-1, -1)
        vc.place_in_bounds(pool.Pool())
        self.assertEqual(vc.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        vc = fishes.Fish(10, 10)
        vc.place_in_bounds(pool.Pool())
        self.assertEqual(vc.get_pos(), [9, 9])


class TestPredator(unittest.TestCase):
    def test_predator(self):
        pr = fishes.Predator(2, 3)
        self.assertEqual(repr(pr), 'P')

    def test_predator_pos(self):
        pr = fishes.Predator(2, 3)
        self.assertEqual(pr.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, m):
        p = pool.Pool()
        m.side_effect = 1, 1, 5, 5
        p.fill(fishes.Victim, 1)
        p.fill(fishes.Predator, 1)
        p._fishes[1].move(p)
        self.assertEqual(p._fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, m):
        p = pool.Pool()
        m.side_effect = 1, 1, 1, 1
        p.fill(fishes.Predator, 1)
        p.fill(fishes.Victim, 1)
        p._fishes[0].eat(p)
        self.assertEqual(len(p._fishes), 1)


class TestVictim(unittest.TestCase):
    def test_victim(self):
        vc = fishes.Victim(2, 3)
        self.assertEqual(repr(vc), 'V')

    def test_victim_pos(self):
        vc = fishes.Victim(2, 3)
        self.assertEqual(vc.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, m):
        vc = fishes.Victim(2, 3)
        m.side_effect = 1, 1
        vc.move(pool.Pool())
        self.assertEqual(vc.get_pos(), [3, 4])
