import garden_map_2 as gm

# Unit tests
import unittest

class TestGardenMap(unittest.TestCase):
    def test_example_1(self):
        map_data = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]
        garden_map = gm.GardenMap(map_data)
        self.assertEqual(garden_map.calculate_total_price(), 80)

    def test_example_2(self):
        map_data = [
            "OOOOO",
            "OXOXO",
            "OOOOO",
            "OXOXO",
            "OOOOO"
        ]
        garden_map = gm.GardenMap(map_data)
        self.assertEqual(garden_map.calculate_total_price(), 436)

    def test_example_3(self):
        map_data = [
            "EEEEE",
            "EXXXX",
            "EEEEE",
            "EXXXX",
            "EEEEE"
        ]
        garden_map = gm.GardenMap(map_data)
        self.assertEqual(garden_map.calculate_total_price(), 236)

    def test_example_4(self):
        map_data = [
            "AAAAAA",
            "AAABBA",
            "AAABBA",
            "ABBAAA",
            "ABBAAA",
            "AAAAAA"
        ]
        garden_map = gm.GardenMap(map_data)
        self.assertEqual(garden_map.calculate_total_price(), 368)

    def test_example_5(self):
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
        self.assertEqual(garden_map.calculate_total_price(), 1206)

    def test_boundary_case_empty(self):
        map_data = []
        garden_map = gm.GardenMap(map_data)
        self.assertEqual(garden_map.calculate_total_price(), 0)

    def test_boundary_case_single_plot(self):
        map_data = ["A"]
        garden_map = gm.GardenMap(map_data)
        self.assertEqual(garden_map.calculate_total_price(), 1 * 4)

if __name__ == "__main__":
    unittest.main()