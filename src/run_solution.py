import argparse
import time
from pathlib import Path

import browser_cookie3
import numpy as np
import requests
from tqdm import tqdm

main_dict = {}
for day in range(1, 26):
    if Path(f"src/day{day}.py").exists():
        exec(f"from day{day} import main as day{day}", globals())
        main_dict[day] = eval(f"day{day}")


def _run_solution(day: int, trials: int, big_data: bool, sample_data: bool):
    print(f"Day {day}:")
    if day not in main_dict:
        print(f"  - Solution for day {day} does not exist!")
    else:
        data = _get_input_data(day=day, big_data=big_data, sample_data=sample_data)
        print(f"  - Running day {day} solution {trials} times...")
        times = []
        for _ in tqdm(range(trials), leave=False):
            start = time.time()
            part_1, part_2 = main_dict[day](data.copy())
            end = time.time()
            times.append(end - start)
        print("  - Part 1: ", part_1, "Part 2: ", part_2)
        print(
            f"  - Complete! After {trials} trials, average time (s): {np.mean(times):.4f} +/- {np.std(times):.4f}"
        )


def _get_input_data(day: int, big_data: bool, sample_data: bool) -> list:
    data_dir = Path(f"data/{day}")
    data_dir.mkdir(exist_ok=True, parents=True)

    if big_data:
        filename = f"day{day:02d}_big_input.txt"
        if not (data_dir / filename).exists():
            raise ValueError(f"Big input data for day {day} does not exist!")

    elif sample_data:
        filename = "sample.txt"
        if not (data_dir / filename).exists():
            raise ValueError(f"Sample data for day {day} does not exist!")

    else:
        filename = "input.txt"
        if not (data_dir / filename).exists():
            raise ValueError(f"Challenge data for day {day} does not exist!")

    # read data into list of strings
    with open(data_dir / filename) as f:
        data = f.read().splitlines()

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC 2023")
    parser.add_argument(
        "-t", "--trials", help="How many times to run the solution", type=int, default=5
    )

    data_type = parser.add_mutually_exclusive_group()
    data_type.add_argument(
        "-b",
        "--big-data",
        help="Use big input (requires offline files)",
        action="store_true",
    )

    data_type.add_argument(
        "-s",
        "--sample-data",
        help="Use sample input (requires offline files)",
        action="store_true",
    )

    parser.add_argument(
        "-a", "--all", help="Run all days (`days` is ignored)", action="store_true"
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
        for day in range(1, 26):
            _run_solution(
                day=day,
                trials=args.trials,
                big_data=args.big_data,
                sample_data=args.sample_data,
            )

    else:
        for day in args.days:
            _run_solution(
                day=day,
                trials=args.trials,
                big_data=args.big_data,
                sample_data=args.sample_data,
            )
