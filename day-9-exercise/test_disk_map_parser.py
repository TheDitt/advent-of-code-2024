


# Unit tests
import unittest
import disk_map_parser as dmp

class TestDiskMapParser(unittest.TestCase):
    def test_parse(self):
        parser = dmp.DiskMapParser("2333133121414131402")
        expected_output = [(2, 1), (3, 3), (1, 1), (3, 1), 
                           (3, 1), (2, 1), (1, 1), (4, 1), 
                           (1, 1), (4, 1), (1, 1), (3, 1), 
                           (1, 1), (4, 1), (0, 1), (2, 1)]
        self.assertEqual(parser.parse(), expected_output)

    def test_empty_map(self):
        parser = dmp.DiskMapParser("")
        expected_output = []
        self.assertEqual(parser.parse(), expected_output)

    def test_single_block(self):
        parser = dmp.DiskMapParser("5")
        expected_output = [(5, 1)]
        self.assertEqual(parser.parse(), expected_output)

    def test_multiple_identical_blocks(self):
        parser = dmp.DiskMapParser("5555")
        expected_output = [(5, 4)]
        self.assertEqual(parser.parse(), expected_output)

    def test_alternating_blocks(self):
        parser = dmp.DiskMapParser("121212")
        expected_output = [(1, 1), (2, 1), (1, 1), (2, 1), (1, 1), (2, 1)]
        self.assertEqual(parser.parse(), expected_output)

    def test_simple_sequence_blocks(self):
        parser = dmp.DiskMapParser("12345")
        expected_output = [(1, 1), (2, 1), (1, 1), (2, 1), (1, 1), (2, 1)]
        self.assertEqual(parser.parse(), expected_output)

if __name__ == "__main__":
    unittest.main()
