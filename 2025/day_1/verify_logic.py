"""Detailed trace to verify the logic"""

def trace_rotation(position, direction, steps):
    """Trace a single rotation and count zero crossings"""
    print(f"\nPosition: {position}, Rotation: {direction}{steps}")

    if direction == "R":
        # Moving right (increasing)
        new_pos = (position + steps) % 100
        total_distance = position + steps

        # How many times do we cross 0?
        # If we start at 50 and go 60 steps: 50+60=110, we cross 0 once (at 100/0)
        # If we start at 50 and go 160 steps: 50+160=210, we cross 0 twice (at 100 and 200)
        zeros_crossed = total_distance // 100

        print(f"  Right: {position} + {steps} = {total_distance}")
        print(f"  New position: {new_pos}")
        print(f"  Zeros crossed: {zeros_crossed}")

        return new_pos, zeros_crossed
    else:
        # Moving left (decreasing)
        new_pos = (position - steps) % 100

        if position < steps:
            # We go negative, crossing 0
            # Example: position=5, steps=10 -> 5-10=-5
            # We cross 0 once going from 5->0->99->95
            # Example: position=5, steps=110 -> 5-110=-105
            # We cross 0 twice: 5->0->99->...->0->99->95

            zeros_crossed = (steps - position + 99) // 100
            print(f"  Left: {position} - {steps} = {position - steps}")
            print(f"  New position: {new_pos}")
            print(f"  Zeros crossed: {zeros_crossed}")
        else:
            zeros_crossed = 0
            print(f"  Left: {position} - {steps} = {position - steps}")
            print(f"  New position: {new_pos}")
            print(f"  No zeros crossed")

        return new_pos, zeros_crossed

# Test with the example
position = 50
total_crosses = 0
landed_on_zero = 0

rotations = [
    ("L", 68),   # Should cross 0 once
    ("L", 30),   # No cross
    ("R", 48),   # Should end on 0 (and cross it)
    ("L", 5),    # From 0, should cross once
    ("R", 60),   # Should cross 0 once
    ("L", 55),   # Should end on 0 (no crossing during)
    ("L", 1),    # From 0, should cross once
    ("L", 99),   # Should end on 0 (no crossing during)
    ("R", 14),   # No cross
    ("L", 82),   # Should cross once
]

for direction, steps in rotations:
    position, crosses = trace_rotation(position, direction, steps)
    total_crosses += crosses
    if position == 0:
        landed_on_zero += 1
        print(f"  *** LANDED ON ZERO ***")

print(f"\n=== FINAL RESULTS ===")
print(f"Final position: {position}")
print(f"Landed on zero: {landed_on_zero} times")
print(f"Total zero crosses (Part 2): {total_crosses}")
print(f"\nExpected: landed=3, crosses=6")
