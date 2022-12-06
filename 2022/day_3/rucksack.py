#!/usr/bin/env python
""" Rock Paper Scissor"""


import argparse
import string
from typing import Dict


LETTER_TO_NUMBER={letter: _id + 1 for _id, letter in enumerate(string.ascii_letters)}
def main(args):
    with open(args.input,"r") as handle_r:
        item_score = 0
        line_counter = 1
        three_elfs_group = []
        three_elfs_item_score = 0
        for line in handle_r:
            line = line.strip()
            three_elfs_group.append(list(line))

            # Part - 1
            firstpart, secondpart = list(line[:int(len(line)/2)]), list(line[int(len(line)/2):])
            common_item = set(firstpart).intersection(secondpart)
            item_score += LETTER_TO_NUMBER[next(iter(common_item))]

            # Part - 2
            if line_counter and line_counter % 3 == 0 and three_elfs_group:
                _1, _2, _3 = three_elfs_group
                common_item = set(_1).intersection(_2).intersection(_3)
                three_elfs_item_score += LETTER_TO_NUMBER[next(iter(common_item))]
                three_elfs_group = []

            line_counter += 1

        print(f"Socre: {item_score}")
        print(f"Three Elfs Item Score: {three_elfs_item_score}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments to Elf calorie task")

    parser.add_argument("input", type=str, help="Path to the Elf calorie list file")

    main(parser.parse_args())
