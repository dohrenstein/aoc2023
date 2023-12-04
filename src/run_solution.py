import argparse
import time
from pathlib import Path

import browser_cookie3
import numpy as np
import requests
from tqdm import tqdm

from day1 import main as day1
from day2 import main as day2
from day3 import main as day3
from day4 import main as day4

main_dict = {
    1: day1,
    2: day2,
    3: day3,
    4: day4,
}


def _run_solution(day: int, trials: int, big_data: bool):
    data = _get_input_data(day=day, big_data=big_data)
    print(f"Running day {day} solution {trials} times...")
    times = []
    for _ in tqdm(range(trials), leave=False):
        start = time.time()
        part_1, part_2 = main_dict[day](data)
        end = time.time()
        times.append(end - start)
    print("Part 1: ", part_1)
    print("Part 2: ", part_2)
    print(
        f"Complete! After {trials} trials, average time (s): {np.mean(times):.4f} +/- {np.std(times):.4f}"
    )


def _get_input_data(day: int, big_data: bool) -> list:
    data_dir = Path(f"data/{day}")
    data_dir.mkdir(exist_ok=True, parents=True)

    if big_data:
        filename = f"day{day:02d}_big_input.txt"
        if not (data_dir / filename).exists():
            raise ValueError(f"Big input data for day {day} does not exist!")

    else:
        filename = f"input.txt"
        # download data if not already present
        if not (data_dir / filename).exists():
            print("Downloading data...")
            cookies = browser_cookie3.chrome(domain_name="adventofcode.com")
            input_data = requests.get(
                f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies
            ).text
            with open(data_dir / "input.txt", "w") as f:
                f.write(input_data)
            print("Complete!")

    # read data into list of strings
    with open(data_dir / filename) as f:
        data = f.read().splitlines()

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="AOC 2023", description="Runs Daniel Ohrenstein's solutions for AOC 2023"
    )
    parser.add_argument(
        "-t", "--trials", help="How many times to run the solution", type=int, default=5
    )
    parser.add_argument(
        "-b",
        "--big-data",
        help="Use big input (requires offline files)",
        action="store_true",
    )
    parser.add_argument(
        "-a", "--all", help="Run all days (`day` is ignored)", action="store_true"
    )
    parser.add_argument(
        "days",
        help="Which challenges to run",
        metavar="days",
        choices=range(1, 26),
        type=int,
        nargs="*",
    )

    args = parser.parse_args()

    if not args.all and len(args.days) == 0:
        print(
            "AOC 2023: error: At least one value must be passed to `days` (or use `--all` to run all solutions)"
        )
        exit()

    if args.all:
        for day in main_dict.keys():
            _run_solution(day=day, trials=args.trials, big_data=args.big_data)

    else:
        for day in args.days:
            _run_solution(day=day, trials=args.trials, big_data=args.big_data)
