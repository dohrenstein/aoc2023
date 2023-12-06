import re

import numpy as np

from utils import BaseSolution


class Solution(BaseSolution):
    def part_1(self, data: list) -> int:
        result = 1
        times = [int(val) for val in re.findall(r"\d+", data[0])]
        distances = [int(val) for val in re.findall(r"\d+", data[1])]
        for race_time, race_distance in zip(times, distances):
            wait_times = np.arange(race_time, dtype="int64")
            distances = wait_times * (race_time - wait_times)
            result *= (distances > race_distance).sum()

        return result

    def part_2(self, data: list) -> int:
        result = 0

        race_time = int("".join(re.findall(r"\d+", data[0])))
        race_distance = int("".join(re.findall(r"\d+", data[1])))

        wait_times = np.arange(race_time, dtype="int64")
        distances = wait_times * (race_time - wait_times)
        result = (distances > race_distance).sum()

        return result
