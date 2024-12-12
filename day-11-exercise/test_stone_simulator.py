import unittest
import stone_simulator as SS

class TestStoneSimulation(unittest.TestCase):
    def test_single_zero_stone(self):
        initial_stones = [0]
        blinks = 1
        result = SS.StoneSimulator.simulate_stones(initial_stones, blinks)
        self.assertEqual(result, 1, "Failed on single zero stone with 1 blink")

    def test_even_digit_split(self):
        initial_stones = [1234]
        blinks = 1
        result = SS.StoneSimulator.simulate_stones(initial_stones, blinks)
        self.assertEqual(result, 2, "Failed on even digit stone split with 1 blink")

    def test_odd_digit_multiplication(self):
        initial_stones = [123]
        blinks = 1
        result = SS.StoneSimulator.simulate_stones(initial_stones, blinks)
        self.assertEqual(result, 1, 
                         "Failed on odd digit stone multiplication with 1 blink")

    def test_multiple_stones(self):
        initial_stones = [0, 1234, 123]
        blinks = 1
        result = SS.StoneSimulator.simulate_stones(initial_stones, blinks)
        self.assertEqual(result, 4, "Failed on multiple stones with 1 blink")

    def test_multiple_blinks(self):
        initial_stones = [0, 1234, 123]
        blinks = 2
        result = SS.StoneSimulator.simulate_stones(initial_stones, blinks)
        self.assertEqual(result, 7, "Failed on multiple stones with 2 blinks")

    def test_large_number_of_blinks(self):
        initial_stones = [0, 5601550, 3914, 852, 50706, 68, 6, 645371]
        blinks = 75
        result = SS.StoneSimulator.simulate_stones(initial_stones, blinks)
        print(result)
        self.assertEqual(result, 224869647102559, "Failed on large number of blinks")

if __name__ == '__main__':
    unittest.main()
