"""Test module"""
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """Test pool class"""
    def setUp(self) -> None:
        """setup test class"""
        self.place = pool.Pool()

    def test_pool(self):
        """Test pool on size"""
        self.assertEqual(self.place.get_size(), (10, 10),
                         "Pool size doesn't equal 10x10")

    def test_fill_predators(self):
        """Fill a pool with predators"""
        predators_quantity = 3
        length = len(self.place.fishes)
        self.place.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.place.fishes), length + predators_quantity)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, make):
        """Fill predators random way"""
        make.side_effect = 0, 1
        self.place.fill(fishes.Predator, 1)
        self.assertEqual(self.place.fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, make):
        """Test a victim"""
        make.side_effect = 1, 1, 5, 5, 9, 0
        self.place.fill(fishes.Victim, 3)
        self.assertEqual(self.place.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.place.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, make):
        """Test kill a victim"""
        make.side_effect = 1, 1
        self.place.fill(fishes.Victim, 1)
        self.assertEqual(self.place.get_victim([1, 1]),
                         [self.place.fishes[0]])

    def tearDown(self) -> None:
        """close tests"""


class TestFish(unittest.TestCase):
    """Test fish class"""
    def test_fish_is_in_bounds1(self):
        """fish bounds test"""
        fish_victim = fishes.Fish(-1, -1)
        fish_victim.place_in_bounds(pool.Pool())
        self.assertEqual(fish_victim.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """fish bounds test 2 """
        fish_victim = fishes.Fish(10, 10)
        fish_victim.place_in_bounds(pool.Pool())
        self.assertEqual(fish_victim.get_pos(), [9, 9])


class TestPredator(unittest.TestCase):
    """Test predator class"""
    def test_predator(self):
        """test predator"""
        fish_predator = fishes.Predator(2, 3)
        self.assertEqual(repr(fish_predator), 'P')

    def test_predator_pos(self):
        """test predator position"""
        fish_predator = fishes.Predator(2, 3)
        self.assertEqual(fish_predator.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, make):
        """test predator movement"""
        place = pool.Pool()
        make.side_effect = 1, 1, 5, 5
        place.fill(fishes.Victim, 1)
        place.fill(fishes.Predator, 1)
        place.fishes[1].move(place)
        self.assertEqual(place.fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, make):
        """test predator eating"""
        place = pool.Pool()
        make.side_effect = 1, 1, 1, 1
        place.fill(fishes.Predator, 1)
        place.fill(fishes.Victim, 1)
        place.fishes[0].eat(place)
        self.assertEqual(len(place.fishes), 1)


class TestVictim(unittest.TestCase):
    """Victim test class"""
    def test_victim(self):
        """Victim test"""
        fish_victim = fishes.Victim(2, 3)
        self.assertEqual(repr(fish_victim), 'V')

    def test_victim_pos(self):
        """Victim position test"""
        fish_victim = fishes.Victim(2, 3)
        self.assertEqual(fish_victim.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, make):
        """Victim's movement"""
        fish_victim = fishes.Victim(2, 3)
        make.side_effect = 1, 1
        fish_victim.move(pool.Pool())
        self.assertEqual(fish_victim.get_pos(), [3, 4])
