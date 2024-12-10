class AntennaMap:
    def __init__(self, map_data):
        self.map_data = map_data
        self.antennas = self._parse_map()

    def _parse_map(self):
        antennas = {}
        for y, row in enumerate(self.map_data):
            for x, char in enumerate(row):
                if char.isalnum():  # Check if the character is a letter or digit
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((x, y))
        
        print(antennas)
        return antennas

    def calculate_unique_antinodes(self):
        unique_antinodes = set()
        for frequency, positions in self.antennas.items():
            n = len(positions)
            for i in range(n):
                for j in range(i + 1, n):
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]
                    # Calculate potential antinode positions
                    antinode1 = (x1 + (x2 - x1), y1 + (y2 - y1))
                    antinode2 = (x1 - (x2 - x1), y1 - (y2 - y1))
                    # Check if within bounds
                    if self._is_within_bounds(antinode1):
                        unique_antinodes.add(antinode1)
                    if self._is_within_bounds(antinode2):
                        unique_antinodes.add(antinode2)
        return len(unique_antinodes)

    def _is_within_bounds(self, position):
        x, y = position
        return 0 <= x < len(self.map_data[0]) and 0 <= y < len(self.map_data)
