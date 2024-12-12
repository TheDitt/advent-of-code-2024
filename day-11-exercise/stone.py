class Stone:
    def __init__(self, value):
        self.value = value

    def transform_stone(value):
        if value == 0:
            return 1  # Replaced by a stone with value 1
        elif len(str(value)) % 2 == 0:
            return 2  # Split into two stones
        else:
            return 1  # Replaced by a stone with value multiplied by 2024

