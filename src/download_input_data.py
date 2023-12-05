import argparse
from pathlib import Path
from typing import Iterable, Union

import browser_cookie3
import requests


def main(days: Union[Iterable[int], int]):
    if isinstance(days, int):
        days = [days]

    for day in days:
        print(f"Day {day}:")
        data_dir = Path(f"data/{day}")
        data_dir.mkdir(exist_ok=True, parents=True)

        filename = f"input.txt"
        # download data if not already present
        if (data_dir / filename).exists():
            print("  - Data already exists")
        else:
            print("  - Downloading data...")
            cookies = browser_cookie3.chrome(domain_name="adventofcode.com")
            input_data = requests.get(
                f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies
            ).text
            with open(data_dir / "input.txt", "w") as f:
                f.write(input_data)
            print("  - Complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "days",
        help="Which days' data to download",
        metavar="days",
        choices=range(1, 26),
        type=int,
        nargs="*",
    )
    parser.add_argument(
        "-a", "--all", help="Run all days (`days` is ignored)", action="store_true"
    )

    args = parser.parse_args()
    if args.all:
        main(range(1, 26))
    else:
        main(args.days)
