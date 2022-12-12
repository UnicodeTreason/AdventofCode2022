#!/usr/bin/env python3
# Imports
from pathlib import Path

# Read input
inputPath = Path(__file__).with_name('input_day0201_dev.txt')
with inputPath.open('r') as f:
    inputLines = f.readlines()

# Known Logic:
# 1,A,X,Rock
# 2,B,Y,Paper
# 3,C,Z,Scissors
#
# 0,Loss
# 3,Draw
# 6,Win
# Dev input = 15

# Process input
roundScores = []
for line in inputLines:
    # Strip newline characters
    line = line.strip()

    # Split played shapes
    opponent, player = line.split()

    # Convert char to ASCII code
    opponent = ord(opponent) - 65
    player = ord(player) - 88
    print(f'Opponent: {opponent}, Player: {player}')

    # If Draw
    if opponent == player:
        roundScores.append(player + 3)

print(f'Round Scores: {roundScores}')
print(f'Total: {sum(roundScores)}')
