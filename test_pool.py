'''module'''
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    '''class'''

    def setUp(self) -> None:
        '''def'''
        self.swimming_pool = pool.Pool()

    def test_pool(self):
        '''def'''
        self.assertEqual(self.swimming_pool.get_size(),
                         (20, 20), "Pool size doesn't equal 20x20")

    def test_fill_predators(self):
        '''def'''
        predators_quantity = 3
        length = len(self.swimming_pool.get_fishes())
        self.swimming_pool.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.swimming_pool.get_fishes()),
                         length + predators_quantity)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, mov):
        '''def'''
        mov.side_effect = 0, 1
        self.swimming_pool.fill(fishes.Predator, 1)
        self.assertEqual(self.swimming_pool.get_fishes()[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, mov):
        '''def'''
        mov.side_effect = 1, 1, 5, 5, 9, 0
        self.swimming_pool.fill(fishes.Victim, 3)
        self.assertEqual(self.swimming_pool.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.swimming_pool.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, mov):
        '''def'''
        mov.side_effect = 1, 1
        self.swimming_pool.fill(fishes.Victim, 1)
        self.assertEqual(self.swimming_pool.get_victim([1, 1]),
                         [self.swimming_pool.get_fishes()[0]])

    def tearDown(self) -> None:
        '''pass'''


class TestFish(unittest.TestCase):
    '''class'''

    def test_fish_is_in_bounds1(self):
        '''def'''
        victim = fishes.Fish(-1, -1)
        victim.place_in_bounds(pool.Pool())
        self.assertEqual(victim.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        '''def'''
        victim = fishes.Fish(20, 20)
        victim.place_in_bounds(pool.Pool())
        self.assertEqual(victim.get_pos(), [19, 19])


class TestPredator(unittest.TestCase):
    '''class'''

    def test_predator(self):
        '''def'''
        predator = fishes.Predator(2, 3)
        self.assertEqual(repr(predator), 'P')

    def test_predator_pos(self):
        '''def'''
        predator = fishes.Predator(2, 3)
        self.assertEqual(predator.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, mov):
        '''def'''
        swimming_pool = pool.Pool()
        mov.side_effect = 1, 1, 5, 5
        swimming_pool.fill(fishes.Victim, 1)
        swimming_pool.fill(fishes.Predator, 1)
        swimming_pool.get_fishes()[1].move(swimming_pool)
        self.assertEqual(swimming_pool.get_fishes()[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, mov):
        '''def'''
        swimming_pool = pool.Pool()
        mov.side_effect = 1, 1, 1, 1
        swimming_pool.fill(fishes.Predator, 1)
        swimming_pool.fill(fishes.Victim, 1)
        swimming_pool.get_fishes()[0].eat(swimming_pool)
        self.assertEqual(len(swimming_pool.get_fishes()), 1)


class TestVictim(unittest.TestCase):
    '''class'''

    def test_victim(self):
        '''def'''
        victim = fishes.Victim(2, 3)
        self.assertEqual(repr(victim), 'V')

    def test_victim_pos(self):
        '''def'''
        victim = fishes.Victim(2, 3)
        self.assertEqual(victim.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, mov):
        '''def'''
        victim = fishes.Victim(2, 3)
        mov.side_effect = 1, 1
        victim.move(pool.Pool())
        self.assertEqual(victim.get_pos(), [3, 4])
