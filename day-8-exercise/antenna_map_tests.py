# Unit test cases
import unittest
import antenna_map as AM

class TestAntennaMap(unittest.TestCase):
    def test_unique_antinodes(self):
        map_data = [
            "......#....#",
            "...#....0...",
            "....#0....#.",
            "..#....0....",
            "....0....#..",
            ".#....A.....",
            "...#........",
            "#......#....",
            "........A...",
            ".........A..",
            "..........#.",
            "..........#."
        ]
        antenna_map = AM.AntennaMap(map_data)
        self.assertEqual(antenna_map.calculate_unique_antinodes(), 14)

    def test_no_antennas(self):
        map_data = [
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]
        antenna_map = AM.AntennaMap(map_data)
        self.assertEqual(antenna_map.calculate_unique_antinodes(), 0)

    def test_single_antenna(self):
        map_data = [
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "....0.....",
            "..........",
            "..........",
            "..........",
            ".........."
        ]
        antenna_map = AM.AntennaMap(map_data)
        self.assertEqual(antenna_map.calculate_unique_antinodes(), 0)

if __name__ == "__main__":
    unittest.main()
