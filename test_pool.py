"""TEST POOL"""
import unittest
import unittest.mock
import pool
import fishes


class TestPool(unittest.TestCase):
    """test pool class"""
    def setUp(self) -> None:
        """setUP"""
        self.p_n = pool.Pool()

    def test_pool(self):
        """TEST POOL"""
        self.assertEqual(self.p_n.get_size(), (20, 20),
                         "Pool size doesn't equal 20x20")

    def test_fill_predators(self):
        """test fill predators"""
        pre_count = 3
        len_ = len(self.p_n._fishes)  # pylint: disable=W0212
        self.p_n.fill(fishes.Predator, pre_count)
        self.assertEqual(len(self.p_n._fishes),  # pylint: disable=W0212
                         len_ + pre_count)

    @unittest.mock.patch('random.randint')
    def test_fill_predators_random(self, m_name):
        """test fill predators random"""
        m_name.side_effect = 0, 1
        self.p_n.fill(fishes.Predator, 1)
        self.assertEqual(self.p_n._fishes[0].get_pos(),  # pylint:disable=W0212
                         [0, 1])

    @unittest.mock.patch('random.randint')
    def test_nearest_victim(self, m_name):
        """test nearest victim"""
        m_name.side_effect = 1, 1, 5, 5, 9, 0
        self.p_n.fill(fishes.Victim, 3)
        self.assertEqual(self.p_n.get_nearest_victim(2, 2),
                         (1, 1))
        self.assertEqual(self.p_n.get_nearest_victim(8, 1),
                         (9, 0))

    @unittest.mock.patch('random.randint')
    def test_get_victim(self, m_name):
        """test get victim"""
        m_name.side_effect = 1, 1
        self.p_n.fill(fishes.Victim, 1)
        self.assertEqual(self.p_n.get_victim([1, 1]),
                         [self.p_n._fishes[0]])  # pylint: disable=W0212

    def tearDown(self) -> None:
        """tears down"""


class TestFish(unittest.TestCase):
    """test fish"""
    def test_fish_is_in_bounds1(self):
        """is in bound 1 ?"""
        vc_name = fishes.Fish(-1, -1)
        vc_name.place_in_bounds(pool.Pool())
        self.assertEqual(vc_name.get_pos(), [0, 0])

    def test_fish_is_in_bounds2(self):
        """is in bound 2 ?"""
        vc_name = fishes.Fish(20, 20)
        vc_name.place_in_bounds(pool.Pool())
        self.assertEqual(vc_name.get_pos(), [19, 19])


class TestPredator(unittest.TestCase):
    """class test predator"""
    def test_predator(self):
        """test predator"""
        pr_name = fishes.Predator(2, 3)
        self.assertEqual(repr(pr_name), 'P')

    def test_predator_pos(self):
        """test predator pos"""
        pr_name = fishes.Predator(2, 3)
        self.assertEqual(pr_name.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_move(self, m_name):
        """test predator move"""
        p_n = pool.Pool()
        m_name.side_effect = 1, 1, 5, 5
        p_n.fill(fishes.Victim, 1)
        p_n.fill(fishes.Predator, 1)
        p_n._fishes[1].move(p_n)  # pylint: disable=W0212
        self.assertEqual(p_n._fishes[1].get_pos(),  # pylint: disable=W0212
                         [3, 3])

    @unittest.mock.patch('random.randint')
    def test_predator_eating(self, m_name):
        """test predator eating"""
        p_n = pool.Pool()
        m_name.side_effect = 1, 1, 1, 1
        p_n.fill(fishes.Predator, 1)
        p_n.fill(fishes.Victim, 1)
        p_n._fishes[0].eat(p_n)  # pylint: disable=W0212
        self.assertEqual(len(p_n._fishes), 1)  # pylint: disable=W0212


class TestVictim(unittest.TestCase):
    """CLASS TEST VICTIM"""
    def test_victim(self):
        """test victim"""
        vc_name = fishes.Victim(2, 3)
        self.assertEqual(repr(vc_name), 'V')

    def test_victim_pos(self):
        """pos"""
        vc_name = fishes.Victim(2, 3)
        self.assertEqual(vc_name.get_pos(), [2, 3])

    @unittest.mock.patch('random.randint')
    def test_victim_correct_move(self, m_name):
        """correct move"""
        vc_name = fishes.Victim(2, 3)
        m_name.side_effect = 1, 1
        vc_name.move(pool.Pool())
        self.assertEqual(vc_name.get_pos(), [3, 4])
