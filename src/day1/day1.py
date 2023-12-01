import regex as re

with open("input.txt") as f:
    data = f.read().splitlines()

part_1 = 0
for row in data:
    digits = re.sub("[a-zA-Z]+", "", row)
    part_1 += int(digits[0] + digits[-1])

print("Part 1: ", part_1)

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

part_2 = 0
for row in data:
    m = re.findall(
        r"one|two|three|four|five|six|seven|eight|nine|\d", row, overlapped=True
    )
    for i, digit in enumerate(m):
        if digit in mapping:
            m[i] = mapping[digit]
    part_2 += int(m[0] + m[-1])

print("Part 2: ", part_2)
