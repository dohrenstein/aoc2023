import regex as re

from utils import BaseSolution


class Solution(BaseSolution):
    def part_1(self, data: list) -> int:
        result = 0

        for row in data:
            game_number = re.findall(r"Game (\d+):", row)[0]
            turns = row.split(": ")[1].split("; ")
            part_1_possible = True
            for turn in turns:
                part_1_cubes_remaining = {"red": 12, "green": 13, "blue": 14}
                groups = turn.split(", ")
                for group in groups:
                    quantity, colour = group.split(" ")
                    part_1_cubes_remaining[colour] -= int(quantity)

                if any(value < 0 for value in part_1_cubes_remaining.values()):
                    part_1_possible = False

            if part_1_possible:
                result += int(game_number)
        return result

    def part_2(self, data: list) -> int:
        result = 0
        for row in data:
            part_2_min_cubes_required = {"red": 0, "green": 0, "blue": 0}
            turns = row.split(": ")[1].split("; ")
            for turn in turns:
                groups = turn.split(", ")
                for group in groups:
                    quantity, colour = group.split(" ")
                    if part_2_min_cubes_required[colour] < int(quantity):
                        part_2_min_cubes_required[colour] = int(quantity)

            power = 1
            for value in part_2_min_cubes_required.values():
                power *= value
            result += power

        return result
