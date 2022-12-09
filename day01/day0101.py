#!/usr/bin/env python3
# Imports
from pathlib import Path

# Read input
inputPath = Path(__file__).with_name('day0101.txt')
with inputPath.open('r') as f:
    inputLines = f.readlines()


# Define Elf
class Elf:

    def __init__(self, calories=[200, 400]):
        self.calories = calories
        self.caloriesTotal = sum(calories)

    def get_calories_total(self):
        print(f'Calories: {self.caloriesTotal}')

    def get_calories_raw(self):
        print(f'Calories: {self.calories}')


# Process input
elfCount = 0
for line in inputLines:
    # Strip newline characters
    line = line.strip()

    # Increment Elf
    if line == '':
        print(f'ELF{elfCount} INIT')
        elfCount += 1
        continue

    print(f'It Number: {line}')

# JimTheElf = Elf()
# JimTheElf.get_calories_raw()
# JimTheElf.get_calories_total()
