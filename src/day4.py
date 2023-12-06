import re

import numpy as np

from utils import BaseSolution


class Solution(BaseSolution):
    def part_1(self, data: list) -> int:
        result = 0

        list_matches = []
        for card in data:
            card = card.split(": ")[1].split(" | ")
            winning_numbers = re.findall(r"\d+", card[0])
            numbers_we_have = re.findall(r"\d+", card[1])
            n_matches = set(numbers_we_have).intersection(winning_numbers)
            list_matches.append(len(n_matches))
            if len(n_matches) >= 1:
                result += 2 ** (len(n_matches) - 1)

        return result

    def part_2(self, data: list) -> int:
        result = 0

        list_matches = []
        for card in data:
            card = card.split(": ")[1].split(" | ")
            winning_numbers = re.findall(r"\d+", card[0])
            numbers_we_have = re.findall(r"\d+", card[1])
            n_matches = set(numbers_we_have).intersection(winning_numbers)
            list_matches.append(len(n_matches))

        part_2_num_cards = np.array([1] * len(data), dtype="int64")
        for card in range(len(part_2_num_cards)):
            n_matches = list_matches[card]
            part_2_num_cards[card + 1 : card + 1 + n_matches] += part_2_num_cards[card]

        result = sum(part_2_num_cards)

        return result
