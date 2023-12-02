import time
from typing import Tuple
from tqdm import tqdm

import numpy as np
import regex as re


def main(data: list) -> Tuple[int, int]:
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

    part_1 = 0
    part_2 = 0
    for i, row in enumerate(data):
        m1 = re.findall(r"\d", row, overlapped=True)
        part_1 += int(m1[0] + m1[-1])
        m2 = re.findall(
            r"one|two|three|four|five|six|seven|eight|nine|\d", row, overlapped=True
        )
        for i, digit in enumerate(m2):
            if digit in mapping:
                m2[i] = mapping[digit]
        part_2 += int(m2[0] + m2[-1])

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
