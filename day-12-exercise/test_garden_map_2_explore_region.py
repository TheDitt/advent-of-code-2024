import unittest
import garden_map_2 as gm

class TestGardenMapExploreRegion(unittest.TestCase):
    def setUp(self):
        # This setup runs before each test method
        self.map_data = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]
        self.garden_map = gm.GardenMap(self.map_data)

    def test_explore_region_A(self):
        # Test exploring a region starting from (0, 0) which is 'A'
        area, sides = self.garden_map.explore_region(0, 0, 'A')
        self.assertEqual(area, 4)  # 'AAAA' is a 4-cell region
        self.assertEqual(sides, 8)  # Each 'A' has 2 sides exposed

    def test_explore_region_B(self):
        # Test exploring a region starting from (1, 0) which is 'B'
        area, sides = self.garden_map.explore_region(1, 0, 'B')
        self.assertEqual(area, 3)  # 'BB' is a 3-cell region
        self.assertEqual(sides, 8)  # Each 'B' has 2 sides exposed

    def test_explore_region_C(self):
        # Test exploring a region starting from (1, 2) which is 'C'
        area, sides = self.garden_map.explore_region(1, 2, 'C')
        self.assertEqual(area, 4)  # 'CC' is a 4-cell region
        self.assertEqual(sides, 10)  # Each 'C' has 2.5 sides exposed on average

    def test_explore_region_D(self):
        # Test exploring a region starting from (1, 3) which is 'D'
        area, sides = self.garden_map.explore_region(1, 3, 'D')
        self.assertEqual(area, 1)  # 'D' is a single-cell region
        self.assertEqual(sides, 4)  # 'D' has 4 sides exposed

    def test_explore_region_E(self):
        # Test exploring a region starting from (3, 0) which is 'E'
        area, sides = self.garden_map.explore_region(3, 0, 'E')
        self.assertEqual(area, 3)  # 'EEE' is a 3-cell region
        self.assertEqual(sides, 8)  # Each 'E' has 2 sides exposed

if __name__ == "__main__":
    unittest.main()
