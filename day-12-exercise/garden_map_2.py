# class GardenMap:
#     def __init__(self, map_data):
#         self.map = map_data
#         self.rows = len(map_data)
#         self.cols = len(map_data[0]) if self.rows > 0 else 0
#         self.visited = [[False] * self.cols for _ in range(self.rows)]

#     def calculate_total_price(self):
#         total_price = 0
#         for r in range(self.rows):
#             for c in range(self.cols):
#                 if not self.visited[r][c]:
#                     area, sides = self.explore_region(r, c, self.map[r][c])
#                     total_price += area * sides
#         return total_price

#     def explore_region(self, r, c, plant_type):
#         stack = [(r, c)]
#         area = 0
#         sides = 0
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#         while stack:
#             x, y = stack.pop()
#             if self.visited[x][y]:
#                 continue
#             self.visited[x][y] = True
#             area += 1
#             local_sides = 0

#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < self.rows and 0 <= ny < self.cols:
#                     if self.map[nx][ny] == plant_type:
#                         if not self.visited[nx][ny]:
#                             stack.append((nx, ny))
#                     else:
#                         local_sides += 1
#                 else:
#                     local_sides += 1

#             sides += local_sides

#         return area, sides

class GardenMap:
    def __init__(self, map_data):
        self.map = map_data
        self.rows = len(map_data)
        self.cols = len(map_data[0]) if self.rows > 0 else 0
        self.visited = [[False] * self.cols for _ in range(self.rows)]

    def calculate_total_price(self):
        total_price = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.visited[r][c]:
                    area, sides = self.explore_region(r, c, self.map[r][c])
                    total_price += area * sides
        return total_price

    def explore_region(self, r, c, plant_type):
        stack = [(r, c)]
        area = 0
        sides = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while stack:
            x, y = stack.pop()
            if self.visited[x][y]:
                continue
            self.visited[x][y] = True
            area += 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols:
                    if self.map[nx][ny] != plant_type:
                        sides += 1
                else:
                    sides += 1

        return area, sides



