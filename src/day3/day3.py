import re
import time
from typing import Tuple

import numpy as np
from tqdm import tqdm


def main(data: list) -> Tuple[int, int]:
    part_1 = 0
    part_2 = 0

    np_data = np.array([list(row) for row in data])
    digits = set(str(digit) for digit in range(10))
    all_symbols = set(np_data.flat).difference(digits).difference(["."])

    symbol_mask = np.pad(
        np.isin(np_data, list(all_symbols)),
        mode="constant",
        pad_width=(1, 1),
        constant_values=False,
    )

    adjacent_to_symbol_mask = (
        symbol_mask
        | np.roll(symbol_mask, shift=1, axis=0)
        | np.roll(symbol_mask, shift=-1, axis=0)
        | np.roll(symbol_mask, shift=1, axis=1)
        | np.roll(symbol_mask, shift=-1, axis=1)
        | np.roll(symbol_mask, shift=(1, 1), axis=(0, 1))
        | np.roll(symbol_mask, shift=(1, -1), axis=(0, 1))
        | np.roll(symbol_mask, shift=(-1, 1), axis=(0, 1))
        | np.roll(symbol_mask, shift=(-1, -1), axis=(0, 1))
    )[1:-1, 1:-1]

    number_locations = []
    for i, row in enumerate(data):
        number_locations.extend(
            [(i, m.start(), m.end()) for m in re.finditer(r"\d+", row)]
        )

    for number_location in number_locations:
        if (
            adjacent_to_symbol_mask[
                number_location[0], number_location[1] : number_location[2]
            ].sum()
            > 0
        ):
            part_1 += int(
                "".join(
                    np_data[number_location[0], number_location[1] : number_location[2]]
                )
            )

    gear_mask = np.equal(np_data, ["*"])
    adjacent_number_count = np.zeros(np_data.shape)
    for number_location in number_locations:
        adjacent_to_number_location_mask = np.zeros(np_data.shape)
        adjacent_to_number_location_mask[
            max(0, number_location[0] - 1) : number_location[0] + 2,
            max(0, number_location[1] - 1) : number_location[2] + 1,
        ] = 1
        adjacent_number_count += gear_mask * adjacent_to_number_location_mask

    gear_map = np.equal(adjacent_number_count, [2])

    for y_gear, x_gear in list(zip(*gear_map.nonzero())):
        gear_ratio = 1
        for number_location in number_locations:
            if (number_location[0] - 1) <= y_gear <= (number_location[0] + 1) and (
                number_location[1] - 1
            ) <= x_gear <= (number_location[2]):
                gear_ratio *= int(
                    "".join(
                        np_data[
                            number_location[0], number_location[1] : number_location[2]
                        ]
                    )
                )
        part_2 += gear_ratio

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
