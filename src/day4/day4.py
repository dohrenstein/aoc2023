import re
import time
from typing import Tuple

import numpy as np
from tqdm import tqdm


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

    part_2_num_cards = [1] * len(data)
    for card in range(len(part_2_num_cards)):
        n_matches = list_matches[card]
        for copy in range(part_2_num_cards[card]):
            for match in range(n_matches):
                part_2_num_cards[card + 1 + match] += 1

    part_2 = sum(part_2_num_cards)

    return part_1, part_2


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    times = []
    n_trials = 5
    for trial in tqdm(range(n_trials)):
        start = time.time()
        part_1, part_2 = main(data)
        end = time.time()
        times.append(end - start)
    print("Part 1: ", part_1)
    print("Part 2: ", part_2)
    print(
        f"After {n_trials} trials, average time (s): {np.mean(times):.4f} +/- {np.std(times):.4f}"
    )
