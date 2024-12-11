class DiskFragmenter:

    def __init__(self, disk_map):
        self.disk_map = disk_map

    def compact_disk_and_calculate_checksum(self):
        # Parse the disk map into a list of blocks
        blocks = []
        file_id = 0
        i = 0
        while i < len(self.disk_map):
            file_length = int(self.disk_map[i])
            blocks.extend([file_id] * file_length)
            i += 1
            if i < len(self.disk_map):
                free_length = int(self.disk_map[i])
                blocks.extend(['.'] * free_length)
                i += 1
            file_id += 1

        # Compact the disk
        compacted_blocks = []
        for block in blocks:
            if block != '.':
                compacted_blocks.append(block)

        # Calculate the checksum
        checksum = 0
        for position, block in enumerate(compacted_blocks):
            checksum += position * block

        return checksum

# Example usage
# _disk_map = "2333133121414131402"
# checksum = DiskFragmenter.compact_disk_and_calculate_checksum(_disk_map)
# print("Filesystem checksum:", checksum)
