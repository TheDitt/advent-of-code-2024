class DiskMapParser:
    def __init__(self, disk_map):
        self.disk_map = disk_map

    def parse(self):
        parsed_map = []
        current_id = None
        count = 0

        for char in self.disk_map:
            if char.isdigit():
                if current_id is None:
                    current_id = char
                    count = 1
                elif char == current_id:
                    count += 1
                else:
                    parsed_map.append((int(current_id), count))
                    current_id = char
                    count = 1

        if current_id is not None:
            parsed_map.append((int(current_id), count))

        return parsed_map
