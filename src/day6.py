import re
from typing import Tuple

import numpy as np


def main(data: list) -> Tuple[int, int]:
    part_1 = 1
    part_2 = 0

    # part 1
    times = [int(val) for val in re.findall(r"\d+", data[0])]
    distances = [int(val) for val in re.findall(r"\d+", data[1])]
    for race_time, race_distance in zip(times, distances):
        wait_times = np.arange(race_time, dtype="int64")
        distances = wait_times * (race_time - wait_times)
        part_1 *= (distances > race_distance).sum()

    # part 2
    race_time = int("".join(re.findall(r"\d+", data[0])))
    race_distance = int("".join(re.findall(r"\d+", data[1])))

    wait_times = np.arange(race_time, dtype="int64")
    distances = wait_times * (race_time - wait_times)
    part_2 = (distances > race_distance).sum()

    return part_1, part_2
