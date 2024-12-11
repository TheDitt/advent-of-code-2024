class StoneBlinker:
    def __init__(self, initial_stones):
        self.stones = initial_stones

    def split_number(self, num):
        num_str = str(num)
        mid = len(num_str) // 2
        left = int(num_str[:mid])
        right = int(num_str[mid:])
        return left, right

    def blink(self):
        new_stones = []
        for stone in self.stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                left, right = self.split_number(stone)
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        self.stones = new_stones

    def simulate_blinks(self, num_blinks):
        for _ in range(num_blinks):
            self.blink()
        return self.stones

    def get_stone_count(self):
        return len(self.stones)
