import unittest
import disk_fragmenter as DF

class TestDiskFragmenter(unittest.TestCase):
    
    def test_basic_case(self):
        disk_map = "2333133121414131402"
        expected_checksum = 42  # Replace with the correct expected checksum
        self.assertEqual(DF.DiskFragmenter(disk_map).compact_disk_and_calculate_checksum(),
                         expected_checksum)

    def test_all_files_no_free_space(self):
        disk_map = "111111"
        expected_checksum = 0  # Since there are no free spaces, the checksum should be 0
        self.assertEqual(DF.DiskFragmenter(disk_map).compact_disk_and_calculate_checksum(), 
                         expected_checksum)

    def test_all_free_space(self):
        disk_map = "000000"
        expected_checksum = 0  # No files, so checksum should be 0
        self.assertEqual(DF.DiskFragmenter(disk_map).compact_disk_and_calculate_checksum(), 
                         expected_checksum)

    def test_alternating_files_and_free_space(self):
        disk_map = "101010"
        expected_checksum = 0  # Files are already compacted
        self.assertEqual(DF.DiskFragmenter(disk_map).compact_disk_and_calculate_checksum(),
                        expected_checksum)

    def test_single_file(self):
        disk_map = "100"
        expected_checksum = 0  # Only one file, so checksum is 0
        self.assertEqual(DF.DiskFragmenter(disk_map).compact_disk_and_calculate_checksum(), 
                         expected_checksum)

    def test_single_free_space(self):
        disk_map = "010"
        expected_checksum = 0  # No files, so checksum is 0
        self.assertEqual(DF.DiskFragmenter(disk_map).compact_disk_and_calculate_checksum(), 
                         expected_checksum)

    def test_large_input(self):
        disk_map = "12345678901234567890"
        expected_checksum = 0  # Replace with the correct expected checksum for this input
        self.assertEqual(DF.DiskFragmenter(disk_map).compact_disk_and_calculate_checksum(), 
                         expected_checksum)

    def test_empty_input(self):
        disk_map = ""
        expected_checksum = 0  # No files, so checksum is 0
        self.assertEqual(DF.DiskFragmenter(disk_map).compact_disk_and_calculate_checksum(), 
                         expected_checksum)

if __name__ == '__main__':
    unittest.main()
