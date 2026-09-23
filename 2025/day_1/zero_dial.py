"""
Day 1: Zero Dial
"""

import re
import sys

import click


class Dial:
    """Class to represent a zero dial"""

    def __init__(self, starting_position: int = 50):
        self.position = starting_position
        self._turn_direction = {"L": self.turn_left, "R": self.turn_right}
        self.zero_position_count = 0
        self.zero_hit_count = 0

        self._dial_size = 100

    def _get_turn_direction(self, rotation: str):
        """Rotation is either 'L<steps>' or 'R<steps>'"""
        return self._turn_direction[rotation[0]]

    def turn_right(self, steps: int):
        """Turns the dial by the given number of steps"""
        # Count times we PASS THROUGH 0 during rotation (not counting final position)
        # We pass through 0 each time we complete a full 100-number cycle
        total_distance = self.position + steps
        zeros_passed = total_distance // self._dial_size

        self.zero_hit_count += zeros_passed

        self.position = (self.position + steps) % self._dial_size

    def turn_left(self, steps: int):
        """Turns the dial by the given number of steps"""
        # Count times we PASS THROUGH 0 during rotation (not counting final position)
        self.position = (self.position - steps) % self._dial_size
        if self.position < steps:
            # We go negative, so we pass through 0
            # Calculate how many times we wrap around
            zeros_passed = (steps - self.position + (self._dial_size - 1)) // self._dial_size
            self.zero_hit_count += zeros_passed -1 if self.position == 0 else zeros_passed


    def turn(self, rotation: str):
        """Turns the dial based on the rotation string"""
        steps = int(rotation[1:])
        turn_method = self._get_turn_direction(rotation)
        turn_method(steps)

        # Track when we END on zero (for Part 1)
        if self.position == 0:
            self.zero_position_count += 1


def stream_input(file):
    """Streams input from file line by line"""
    for line in file:
        line = line.strip()
        if not re.match(r"^[LR]\d+$", line):
            print(f"Skipping invalid line: {line}")
        yield line


@click.command()
@click.argument("input_file", type=click.File("r"))
def main(input_file):
    """Entry point of code"""
    dial = Dial()
    for rotation in stream_input(input_file):
        dial.turn(rotation)
    print(
        f"Final position of the dial: {dial.position} and "
        f"hit zero {dial.zero_position_count} times"
        f" and crossed zero {dial.zero_hit_count} times."
    )


if __name__ == "__main__":
    sys.exit(main())  # pylint: disable=no-value-for-parameter
