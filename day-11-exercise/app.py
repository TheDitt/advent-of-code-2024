import stone_blinker as SB
import stone_simulator as SS

initial_stones = [0, 5601550, 3914, 852, 50706, 68, 6, 645371]


#Part 1
blinker = SB.StoneBlinker(initial_stones)
blinker.simulate_blinks(25)
# print(blinker.stones)
print(f"Part 1 count: {blinker.get_stone_count()}")


#Part 2
initial_input = [0, 5601550, 3914, 852, 50706, 68, 6, 645371]
blinks = 75
result = SS.StoneSimulator.simulate_stones(initial_input, blinks)
print(f"Part 2 count: {result}")