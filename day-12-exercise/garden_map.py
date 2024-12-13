class GardenMap:
    def __init__(self, map_data):
        self.map_data = map_data
        self.rows = len(map_data)
        self.cols = len(map_data[0]) if self.rows > 0 else 0
        self.visited = [[False] * self.cols for _ in range(self.rows)]

    def calculate_total_price(self):
        total_price = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.visited[r][c]:
                    area, perimeter = self._explore_region(r, c, self.map_data[r][c])
                    total_price += area * perimeter
        return total_price

    def _explore_region(self, r, c, plant_type):
        stack = [(r, c)]
        area = 0
        perimeter = 0

        while stack:
            x, y = stack.pop()
            if self.visited[x][y]:
                continue

            self.visited[x][y] = True
            area += 1
            sides_exposed = 4

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols:
                    if self.map_data[nx][ny] == plant_type:
                        if not self.visited[nx][ny]:
                            stack.append((nx, ny))
                        sides_exposed -= 1

            perimeter += sides_exposed

        return area, perimeter


