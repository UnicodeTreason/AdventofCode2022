#!/usr/bin/env python3
# Imports
from pathlib import Path

# Read input
inputPath = Path(__file__).with_name('input_day0101.txt')
with inputPath.open('r') as f:
    inputLines = f.readlines()

# Process input
elves = []
elf = 0
for line in inputLines:
    # Strip newline characters
    line = line.strip()

    # Add Elf to group
    if line == '':
        elves.append(elf)
        elf = 0
        continue

    # Add calories to Elf
    elf += int(line)

# EOF, Add last Elf
elves.append(elf)

# Calculate output
elvesTop3 = sorted(elves, reverse=True)[:3]
print(f'Top 3 Elves: {elvesTop3}')
print(f'Top Elves: {sum(elvesTop3)}')
