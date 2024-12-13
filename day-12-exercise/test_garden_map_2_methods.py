import unittest
import garden_map_2 as gm

class TestGardenMapMethods(unittest.TestCase):
    def setUp(self):
        # This setup runs before each test method
        self.map_data = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]
        self.garden_map = gm.GardenMap(self.map_data)

    def test_calculate_total_price(self):
        # Test the calculate_total_price method
        expected_price = 80  # Based on the example provided
        self.assertEqual(self.garden_map.calculate_total_price(), expected_price)

    def test_explore_region(self):
        # Test the _explore_region method directly
        # Note: This is a private method, so typically you wouldn't test it directly.
        # However, for the sake of this exercise, we'll assume it's accessible.
        
        # Test exploring a region starting from (0, 0) which is 'A'
        area, sides = self.garden_map._explore_region(0, 0, 'A')
        self.assertEqual(area, 4)  # 'AAAA' is a 4-cell region
        self.assertEqual(sides, 8)  # Each 'A' has 2 sides exposed

        # Test exploring a region starting from (1, 0) which is 'B'
        area, sides = self.garden_map._explore_region(1, 0, 'B')
        self.assertEqual(area, 3)  # 'BB' is a 3-cell region
        self.assertEqual(sides, 8)  # Each 'B' has 2 sides exposed

    def test_explore_region_edge_case(self):
        # Test edge cases for _explore_region
        # Single plot
        single_plot_map = ["A"]
        single_plot_garden = gm.GardenMap(single_plot_map)
        area, sides = single_plot_garden._explore_region(0, 0, 'A')
        self.assertEqual(area, 1)
        self.assertEqual(sides, 4)

        # Empty map
        empty_map = []
        empty_garden = gm.GardenMap(empty_map)
        self.assertEqual(empty_garden.calculate_total_price(), 0)

if __name__ == "__main__":
    unittest.main()
