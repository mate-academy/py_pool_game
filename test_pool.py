"""Script for testing"""
import unittest
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """Tests for Pool class"""
    def setUp(self) -> None:
        """Creating instance of the class"""
        self.new_pool = pool.Pool()

    def test_pool(self):
        """Should return correct size"""
        self.assertEqual(self.new_pool.get_size(),
                         (10, 10),
                         "Pool size doesn't equal 10x10")

    def test_fill_predators(self):
        """Creates predators to fill the pool"""
        predators_quantity = 3
        amount_fish = len(self.new_pool.fishes)
        self.new_pool.fill(fishes.Predator, predators_quantity)
        self.assertEqual(len(self.new_pool.fishes),
                         amount_fish + predators_quantity)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, make):
        """Random fill with predators"""
        make.side_effect = 0, 1
        self.new_pool.fill(fishes.Predator, 1)
        self.assertEqual(self.new_pool.fishes[0].get_pos(), [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, make):
        """What flavor does victim have?"""
        make.side_effect = 1, 1, 5, 5, 9, 0
        self.new_pool.fill(fishes.Victim, 3)
        self.assertEqual(self.new_pool.get_nearest_victim(2, 2), (1, 1))
        self.assertEqual(self.new_pool.get_nearest_victim(8, 1), (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, make):
        """Get a victim"""
        make.side_effect = 1, 1
        self.new_pool.fill(fishes.Victim, 1)
        self.assertEqual(self.new_pool.get_victim([1, 1]),
                         [self.new_pool.fishes[0]])

    def tearDown(self) -> None:
        pass


class TestFish(unittest.TestCase):
    """Tests for Fish class"""
    def test_fish_is_in_bounds1(self):
        """Test fish in bounds1"""
        fish = fishes.Fish(-1, -1)
        fish.place_in_bounds(pool.Pool())
        self.assertEqual(fish.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """Test fish in bounds2"""
        fish = fishes.Fish(10, 10)
        fish.place_in_bounds(pool.Pool())
        self.assertEqual(fish.get_pos(), [9, 9])


class TestPredator(unittest.TestCase):
    """Tests for Predator subclass"""
    def test_predator(self):
        """Test predator"""
        predator = fishes.Predator(2, 3)
        self.assertEqual(repr(predator), 'P')

    def test_predator_pos(self):
        """Predator position"""
        predator = fishes.Predator(2, 3)
        self.assertEqual(predator.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, make):
        """Predator move"""
        new_pool = pool.Pool()
        make.side_effect = 1, 1, 5, 5
        new_pool.fill(fishes.Victim, 1)
        new_pool.fill(fishes.Predator, 1)
        new_pool.fishes[1].move(new_pool)
        self.assertEqual(new_pool.fishes[1].get_pos(), [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, make):
        """Predator eats"""
        new_pool = pool.Pool()
        make.side_effect = 1, 1, 1, 1
        new_pool.fill(fishes.Predator, 1)
        new_pool.fill(fishes.Victim, 1)
        new_pool.fishes[0].eat(new_pool)
        self.assertEqual(len(new_pool.fishes), 1)


class TestVictim(unittest.TestCase):
    """Tests for Victim subclass"""
    def test_victim(self):
        """Test victim"""
        victim = fishes.Victim(2, 3)
        self.assertEqual(repr(victim), 'V')

    def test_victim_pos(self):
        """Victim position"""
        victim = fishes.Victim(2, 3)
        self.assertEqual(victim.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, make):
        """Victim moves"""
        victim = fishes.Victim(2, 3)
        make.side_effect = 1, 1
        victim.move(pool.Pool())
        self.assertEqual(victim.get_pos(), [3, 4])
