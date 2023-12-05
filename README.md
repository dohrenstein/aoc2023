# AOC 2023

## Installation
Create a new environment, e.g with `conda`:

```bash
conda create -n aoc python
```

Activate the new environment:

```bash
conda activate aoc
```

Install requirements and ipykernel:

```bash
pip install -r requirements.txt
```

## Scripts
Download data:
```bash
python src/download_input_data.py -h
```
```
usage: download_input_data.py [-h] [-a] [days ...]

positional arguments:
  days        Which days' data to download

options:
  -h, --help  show this help message and exit
  -a, --all   Run all days (`days` is ignored)
```

Run solution code:
```bash
python src/run_solution.py -h
```
```
usage: AOC 2023 [-h] [-t TRIALS] [-b | -s] [-a] [days ...]

positional arguments:
  days                  Which challenges to run

options:
  -h, --help            show this help message and exit
  -t TRIALS, --trials TRIALS
                        How many times to run the solution
  -b, --big-data        Use big input (requires offline files)
  -s, --sample-data     Use sample input (requires offline files)
  -a, --all             Run all days (`days` is ignored)
```
