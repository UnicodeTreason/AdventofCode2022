#!/usr/bin/env python3
# Imports
from pathlib import Path
import string

# Read input
inputPath = Path(__file__).with_name('input_dev.txt')
with inputPath.open('r') as f:
    inputLines = f.readlines()

# Process input
for line in inputLines:
    # Strip newline characters
    line = line.strip()

    # Split rucksack into compartments
    compartment1 = line[:len(line) // 2]
    compartment2 = line[len(line) // 2:]

    # Compare compartments with list comprehension
    result = [
        x for x in compartment1 + compartment2
        if x in compartment1 and x in compartment2
    ]

    # Determine priority
    if result[0].isupper():
        priority = ord(result[0]) - 38
    else:
        priority = ord(result[0]) - 96

    print(f'RES: {result[0]} | {priority}')
