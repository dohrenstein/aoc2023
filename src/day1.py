import regex as re

from utils import BaseSolution


class Solution(BaseSolution):
    def part_1(self, data: list) -> int:
        result = 0
        for i, row in enumerate(data):
            m = re.findall(r"\d", row, overlapped=True)
            result += int(m[0] + m[-1])
        return result

    def part_2(self, data: list) -> int:
        result = 0

        mapping = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        for i, row in enumerate(data):
            m = re.findall(
                r"one|two|three|four|five|six|seven|eight|nine|\d", row, overlapped=True
            )
            for i, digit in enumerate(m):
                if digit in mapping:
                    m[i] = mapping[digit]
            result += int(m[0] + m[-1])

        return result
