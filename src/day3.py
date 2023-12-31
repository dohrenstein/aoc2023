import re

import numpy as np

from utils import BaseSolution


class Solution(BaseSolution):
    def part_1(self, data: list) -> int:
        result = 0

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
                result += int(
                    "".join(
                        np_data[
                            number_location[0], number_location[1] : number_location[2]
                        ]
                    )
                )

        return result

    def part_2(self, data: list) -> int:
        result = 0

        np_data = np.array([list(row) for row in data])
        digits = set(str(digit) for digit in range(10))
        all_symbols = set(np_data.flat).difference(digits).difference(["."])

        symbol_mask = np.pad(
            np.isin(np_data, list(all_symbols)),
            mode="constant",
            pad_width=(1, 1),
            constant_values=False,
        )

        number_locations = []
        for i, row in enumerate(data):
            number_locations.extend(
                [(i, m.start(), m.end()) for m in re.finditer(r"\d+", row)]
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
                                number_location[0],
                                number_location[1] : number_location[2],
                            ]
                        )
                    )
            result += gear_ratio

        return result
