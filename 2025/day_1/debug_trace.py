"""Debug trace through the example"""

# Example from puzzle
rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

position = 50
zero_count = 0
cross_count = 0

print(f"Start: position = {position}\n")

for rotation in rotations:
    direction = rotation[0]
    steps = int(rotation[1:])
    old_pos = position

    if direction == "R":
        # Right: going up
        new_pos = (position + steps) % 100
        zeros_crossed = (position + steps) // 100
        cross_count += zeros_crossed
        position = new_pos
        print(f"{rotation}: {old_pos} + {steps} = {old_pos + steps} -> {position} (crossed 0: {zeros_crossed} times)")
    else:
        # Left: going down
        new_pos = (position - steps) % 100
        if position - steps < 0:
            zeros_crossed = (steps - position + 99) // 100
            cross_count += zeros_crossed
            print(f"{rotation}: {old_pos} - {steps} = {old_pos - steps} -> {position} (crossed 0: {zeros_crossed} times)")
        else:
            print(f"{rotation}: {old_pos} - {steps} = {old_pos - steps} -> {new_pos} (no crossing)")
        position = new_pos

    if position == 0:
        zero_count += 1
        print(f"  -> LANDED ON 0")
    print()

print(f"\nFinal: position={position}, landed on 0: {zero_count} times, crossed 0: {cross_count} times")
print(f"Total (Part 2): {zero_count + cross_count}")
