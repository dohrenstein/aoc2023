import re
from typing import Tuple

import numpy as np


def main(data: list) -> Tuple[int, int]:
    part_1 = 0
    part_2 = 0

    list_matches = []
    for card in data:
        card = card.split(": ")[1].split(" | ")
        winning_numbers = re.findall(r"\d+", card[0])
        numbers_we_have = re.findall(r"\d+", card[1])
        n_matches = set(numbers_we_have).intersection(winning_numbers)
        list_matches.append(len(n_matches))
        if len(n_matches) >= 1:
            part_1 += 2 ** (len(n_matches) - 1)

    part_2_num_cards = np.array([1] * len(data), dtype="int64")
    for card in range(len(part_2_num_cards)):
        n_matches = list_matches[card]
        part_2_num_cards[card + 1 : card + 1 + n_matches] += part_2_num_cards[card]

    part_2 = sum(part_2_num_cards)

    return part_1, part_2
