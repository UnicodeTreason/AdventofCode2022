#!/usr/bin/env python3
# Imports
from pathlib import Path

# Read input
inputPath = Path(__file__).with_name('input.txt')
with inputPath.open('r') as f:
    inputLines = f.readlines()

# Process input
for line in inputLines:
    # Strip newline characters
    line = line.strip()
