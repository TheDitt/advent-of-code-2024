import unittest
import stone_blinker as SB

class TestStoneBlinker(unittest.TestCase):
    def test_split_number(self):
        blinker = SB.StoneBlinker([])
        self.assertEqual(blinker.split_number(1234), (12, 34))
        self.assertEqual(blinker.split_number(5678), (56, 78))

    def test_blink_zero(self):
        blinker = SB.StoneBlinker([0])
        blinker.blink()
        self.assertEqual(blinker.stones, [1])

    def test_blink_even_digits(self):
        blinker = SB.StoneBlinker([1234])
        blinker.blink()
        self.assertEqual(blinker.stones, [12, 34])

    def test_blink_odd_digits(self):
        blinker = SB.StoneBlinker([123])
        blinker.blink()
        self.assertEqual(blinker.stones, [123 * 2024])

    def test_simulate_blinks(self):
        initial_stones = [125, 17]
        blinker = SB.StoneBlinker(initial_stones)
        blinker.simulate_blinks(1)
        expected_stones_after_1_blink = [125 * 2024, 1, 7]
        self.assertEqual(blinker.stones, expected_stones_after_1_blink)

    def test_get_stone_count(self):
        initial_stones = [125, 17]
        blinker = SB.StoneBlinker(initial_stones)
        blinker.simulate_blinks(1)
        self.assertEqual(blinker.get_stone_count(), len(blinker.stones))

if __name__ == '__main__':
    unittest.main()