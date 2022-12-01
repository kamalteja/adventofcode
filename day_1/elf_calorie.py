#!/usr/bin/env python
""" Calculates Elf calories"""


import argparse
from typing import Dict, List


class ElfCalorie:
    """Elf calorie"""

    def __init__(self, elf_id: int, calories: List[int]):
        self.elf_id = elf_id
        self.calories = [int(calorie) for calorie in calories]
        self.calorie_count = sum(self.calories)

    def __str__(self) -> str:
        return f"Elf ID: {self.elf_id}\nElf Calorie list: {self.calories}\nElf Total Calorie Count: {self.calorie_count}"


class ElfCaloriesStore:
    """Elf calories store"""

    def __init__(self, elf_calories_store: Dict[int, ElfCalorie]):
        self.elf_calories_store: Dict[int, ElfCalorie] = elf_calories_store or {}

    @classmethod
    def empty_store(cls):
        return cls({})

    @property
    def calorie_count_store(self):
        return {
            eid: e_calorie.calorie_count
            for eid, e_calorie in self.elf_calories_store.items()
        }

    def add_calorie(self, elf_id, food_calories):
        if elf_id in self.elf_calories_store:
            raise ValueError(f"Duplicate elf ID: {elf_id}")

        self.elf_calories_store[elf_id] = ElfCalorie(elf_id, food_calories)


class ElfCalorieStoreStats(ElfCaloriesStore):
    def hight_calorie_elf(self):

        max_c = max(self.calorie_count_store.values())
        for e_id, calorie_count in self.calorie_count_store.items():
            if calorie_count == max_c:
                return self.elf_calories_store[e_id]

    def top_3_elves(self):
        _sorted_calories = sorted(self.calorie_count_store.values(), reverse=True)
        first_elf = None
        second_elf = None
        third_elf = None
        for e_id, calorie_count in self.calorie_count_store.items():
            if calorie_count == _sorted_calories[0]:
                first_elf = self.elf_calories_store[e_id]
            elif calorie_count == _sorted_calories[1]:
                second_elf = self.elf_calories_store[e_id]
            elif calorie_count == _sorted_calories[2]:
                third_elf = self.elf_calories_store[e_id]

        if first_elf is None or second_elf is None or third_elf is None:
            raise ValueError("Failed to compute top 3 elfs")

        return (first_elf, second_elf, third_elf)


def main(args):
    """Entry point of the script"""
    elf_calories_store = ElfCalorieStoreStats.empty_store()

    with open(args.input, "r") as handle_r:
        elf_id = 1
        food_calories = []
        for line in handle_r:
            if not line.strip():
                elf_calories_store.add_calorie(elf_id, food_calories)
                food_calories = []
                elf_id += 1
                continue

            food_calories.append(int(line))

    # Part - 1
    h_elf = elf_calories_store.hight_calorie_elf()
    if h_elf:
        print("Part - 1")
        print(h_elf)
        print("-------------------------------", end="\n\n")

    # Part - 2
    _top_3_elves = elf_calories_store.top_3_elves()
    if _top_3_elves:
        print("Part - 2")
        print("Top Three elves")
        print("---------------")
        _top_3_c_count = 0
        for elf in _top_3_elves:
            print(elf, end="\n\n")
            _top_3_c_count += elf.calorie_count

        print(f"Top Three elves Total count: {_top_3_c_count}")
        print("-------------------------------", end="\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments to Elf calorie task")

    parser.add_argument("input", type=str, help="Path to the Elf calorie list file")

    main(parser.parse_args())
