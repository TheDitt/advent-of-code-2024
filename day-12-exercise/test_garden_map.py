import unittest
import garden_map as gm

class TestGardenMap(unittest.TestCase):
    def test_example_1(self):
        map_data = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]
        garden_map = gm.GardenMap(map_data)
        self.assertEqual(garden_map.calculate_total_price(), 140)

    def test_example_2(self):
        map_data = [
            "OOOOO",
            "OXOXO",
            "OOOOO",
            "OXOXO",
            "OOOOO"
        ]
        garden_map = gm.GardenMap(map_data)
        self.assertEqual(garden_map.calculate_total_price(), 772)

    def test_large_example(self):
        map_data = [
            "RRRRIICCFF",
            "RRRRIICCCF",
            "VVRRRCCFFF",
            "VVRCCCJFFF",
            "VVVVCJJCFE",
            "VVIVCCJJEE",
            "VVIIICJJEE",
            "MIIIIIJJEE",
            "MIIISIJEEE",
            "MMMISSJEEE"
        ]
        garden_map = gm.GardenMap(map_data)
        self.assertEqual(garden_map.calculate_total_price(), 1930)

if __name__ == '__main__':
    unittest.main()
