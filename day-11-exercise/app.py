import stone_blinker as SB

initial_stones = [0, 5601550, 3914, 852, 50706, 68, 6, 645371]
blinker = SB.StoneBlinker(initial_stones)
blinker.simulate_blinks(75)

print(blinker.stones)
print(blinker.get_stone_count())