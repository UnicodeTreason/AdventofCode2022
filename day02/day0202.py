#!/usr/bin/env python3
# Imports
from pathlib import Path

# Read input
inputPath = Path(__file__).with_name('input.txt')
with inputPath.open('r') as f:
    inputLines = f.readlines()

# Define adjacency lists
playerWinList = {'A': 'B', 'B': 'C', 'C': 'A'}
playerLoseList = {'A': 'C', 'B': 'A', 'C': 'B'}
winsList = {1: 3, 2: 1, 3: 2}

# Process input
roundScores = []
for line in inputLines:
    # Strip newline characters
    line = line.strip()

    # Split played shapes
    opponentRAW, playerRAW = line.split()

    # Determine player move
    match playerRAW:
        case 'X':
            playerRAW = playerLoseList[opponentRAW]
        case 'Y':
            playerRAW = opponentRAW
        case 'Z':
            playerRAW = playerWinList[opponentRAW]

    # Convert char to ASCII code
    opponent = ord(opponentRAW) - 64
    player = ord(playerRAW) - 64
    print(f'Opponent: {opponent}, Player: {player}')

    # Draw
    if player == opponent:
        roundScores.append(player + 3)
        continue

    # Win
    if winsList[player] == opponent:
        roundScores.append(player + 6)
        continue
    # Loss
    else:
        roundScores.append(player + 0)
        continue

print(f'Round Scores: {roundScores}')
print(f'Total: {sum(roundScores)}')
