import re

import pandas as pd

from utils import BaseSolution


class Solution(BaseSolution):
    def part_1(self, data: list) -> int:
        items = [
            "seed",
            "soil",
            "fertilizer",
            "water",
            "light",
            "temperature",
            "humidity",
            "location",
        ]

        seeds_to_plant = [int(index) for index in re.findall(r"\d+", data.pop(0))]

        dict_maps = {}
        map_name = ""
        for row in data:
            if row == "":
                continue
            elif len(re.findall(r"\d+", row)) == 0:
                map_name = row.split(" map")[0]

                # store each kind of mapping in a pandas dataframe
                dict_maps[map_name] = pd.DataFrame(
                    columns=[
                        "destination_range_start",
                        "source_range_start",
                        "range_length",
                    ]
                )
            else:
                # add new mappings to new row of pandas dataframe
                destination_range_start, source_range_start, range_length = [
                    int(index) for index in re.findall(r"\d+", row)
                ]
                dict_maps[map_name].loc[len(dict_maps[map_name])] = (
                    destination_range_start,
                    source_range_start,
                    range_length,
                )

        for map in dict_maps.values():
            # calculate end value and shift delta for each mapping
            map["source_range_end"] = map["source_range_start"] + map["range_length"]
            map["delta"] = map["destination_range_start"] - map["source_range_start"]

        location_numbers = []
        for seed in seeds_to_plant:
            source = seed
            destination = 0
            # cycle through each mapping table from seed->...->location
            for source_field, destination_field in zip(items[:-1], items[1:]):
                mapping_name = f"{source_field}-to-{destination_field}"
                mapping = dict_maps[mapping_name].loc[
                    (dict_maps[mapping_name]["source_range_start"] <= source)
                    & (dict_maps[mapping_name]["source_range_end"] > source)
                ]
                if len(mapping) > 0:
                    destination = source + mapping["delta"].values[0]
                else:
                    destination = source
                source = destination

            location_numbers.append(destination)

        result = min(location_numbers)

        return result

    def part_2(self, data: list) -> int:
        items = [
            "seed",
            "soil",
            "fertilizer",
            "water",
            "light",
            "temperature",
            "humidity",
            "location",
        ]

        seeds_to_plant = [int(index) for index in re.findall(r"\d+", data.pop(0))]

        dict_maps = {}
        map_name = ""
        for row in data:
            if row == "":
                continue
            elif len(re.findall(r"\d+", row)) == 0:
                map_name = row.split(" map")[0]

                # store each kind of mapping in a pandas dataframe
                dict_maps[map_name] = pd.DataFrame(
                    columns=[
                        "destination_range_start",
                        "source_range_start",
                        "range_length",
                    ]
                )
            else:
                # add new mappings to new row of pandas dataframe
                destination_range_start, source_range_start, range_length = [
                    int(index) for index in re.findall(r"\d+", row)
                ]
                dict_maps[map_name].loc[len(dict_maps[map_name])] = (
                    destination_range_start,
                    source_range_start,
                    range_length,
                )

        for map in dict_maps.values():
            # calculate end value and shift delta for each mapping
            map["source_range_end"] = map["source_range_start"] + map["range_length"]
            map["delta"] = map["destination_range_start"] - map["source_range_start"]

        # calculate seed ranges for part 2
        part_2_seeds_to_plant = []
        i = 0
        while i < len(seeds_to_plant):
            part_2_seeds_to_plant.append(
                (seeds_to_plant[i], seeds_to_plant[i] + seeds_to_plant[i + 1])
            )
            i += 2

        source_ranges = part_2_seeds_to_plant
        destination_ranges = []
        for source_field, destination_field in zip(items[:-1], items[1:]):
            destination_ranges = []
            mapping_name = f"{source_field}-to-{destination_field}"
            while len(source_ranges) > 0:
                source_range = source_ranges.pop(0)
                mapping = dict_maps[mapping_name]
                if len(mapping) == 0:
                    # if there are no mappings, all values map identically
                    destination_ranges.append(source_range)
                else:
                    for _, row in mapping.iterrows():
                        # calculate overlap between source range and mapping
                        overlap = (
                            max(row["source_range_start"], source_range[0]),
                            min(row["source_range_end"], source_range[1]),
                        )
                        if overlap[0] < overlap[1]:
                            # for the overlap region, the destination values are the same range, adjusted by the delta
                            destination_ranges.append(list(overlap + row["delta"]))
                            # for the regions outside the overlap, we add these as separate source regions as they
                            # might be altered by other mappings
                            if source_range[0] < overlap[0]:
                                source_ranges.append((source_range[0], overlap[0]))
                            if overlap[1] < source_range[1]:
                                source_ranges.append((overlap[1], source_range[1]))
                            # since mapping source ranges do not overlap, we don't need to loop over any further mappings
                            break
                    else:
                        # if range is unaffected by any mappings, all values map identically to the destination
                        destination_ranges.append(source_range)
            source_ranges = destination_ranges

        result = min([destination_range[0] for destination_range in destination_ranges])

        return result
