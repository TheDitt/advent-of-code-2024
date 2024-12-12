import stone as S

class StoneSimulator:
    def __init__(self, initial_stones):
        self.initial_stones = [S.Stone(value) for value in initial_stones]

    def simulate_stones(initial_stones, blinks):
        current_stone_counts = {value: initial_stones.count(value) 
                                for value in set(initial_stones)}

        for _ in range(blinks):
            next_stone_counts = {}
            for value, count in current_stone_counts.items():
                new_stone_count = S.Stone.transform_stone(value)
                if new_stone_count == 1:
                    next_value = 1 if value == 0 else value * 2024
                    if next_value in next_stone_counts:
                        next_stone_counts[next_value] += count
                    else:
                        next_stone_counts[next_value] = count
                elif new_stone_count == 2:
                    mid = len(str(value)) // 2
                    left = int(str(value)[:mid])
                    right = int(str(value)[mid:])
                    for new_value in (left, right):
                        if new_value in next_stone_counts:
                            next_stone_counts[new_value] += count
                        else:
                            next_stone_counts[new_value] = count
            current_stone_counts = next_stone_counts

        return sum(current_stone_counts.values())

