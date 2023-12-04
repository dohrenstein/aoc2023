from typing import Tuple

import regex as re


def main(data: list) -> Tuple[int, int]:
    part_1 = 0
    part_2 = 0
    for row in data:
        part_2_min_cubes_required = {"red": 0, "green": 0, "blue": 0}
        game_number = re.findall(r"Game (\d+):", row)[0]
        turns = row.split(": ")[1].split("; ")
        part_1_possible = True
        for turn in turns:
            part_1_cubes_remaining = {"red": 12, "green": 13, "blue": 14}
            groups = turn.split(", ")
            for group in groups:
                quantity, colour = group.split(" ")
                part_1_cubes_remaining[colour] -= int(quantity)
                if part_2_min_cubes_required[colour] < int(quantity):
                    part_2_min_cubes_required[colour] = int(quantity)

            if any(value < 0 for value in part_1_cubes_remaining.values()):
                part_1_possible = False

        if part_1_possible:
            part_1 += int(game_number)

        power = 1
        for value in part_2_min_cubes_required.values():
            power *= value
        part_2 += power

    return part_1, part_2
