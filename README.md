# Tic-Tac-Toe with Minimax

This is a Tic-Tac-Toe game developed for the Harvard CS50 AI course. The game features an AI opponent that uses the Minimax algorithm to play optimally, making it impossible to beat if both players play optimally.

## Table of Contents
- [Overview](##overview)
- [Project Requirements](##project-requirements)
- [Files](##files)
- [How to Play](#how-to-play)
- [Minimax Algorithm](#minimax-algorithm)
- [Testing and Linting](#testing-and-linting)

## Overview

This project implements a two-player Tic-Tac-Toe game where you can play against an AI. The AI opponent uses the Minimax algorithm to ensure it always makes the optimal move. The graphical interface for the game is powered by the `pygame` library.

## Project Requirements

To run this project, you will need Python 3.12 and the `pygame` library.

### Install Requirements
To install the required packages, navigate to the project directory and run the following command:

```bash
pip3 install -r requirements.txt
```

### Requirements

- Python 3.12
- `pygame` (listed in `requirements.txt`)【11†source】

## Files

- **`tictactoe.py`**: Contains the logic for the Tic-Tac-Toe game, including the Minimax algorithm.
- **`runner.py`**: Contains the code to run the game with a graphical interface using `pygame`.
- **`requirements.txt`**: A file specifying the required Python libraries.

## How to Play

1. Clone or download the project files.
2. Install the required packages by running:
   ```bash
   pip3 install -r requirements.txt
   ```
3. To start the game, run:
   ```bash
   python runner.py
   ```
4. Play against the AI by selecting the positions for your moves on the board. The AI will respond with its optimal moves.

## Minimax Algorithm

The AI uses the Minimax algorithm to determine the best possible move in every game state. Here's a breakdown of the functions implemented:

- **`player(board)`**: Determines whose turn it is (X or O).
- **`actions(board)`**: Returns all available moves.
- **`result(board, action)`**: Returns the new board state after making a move.
- **`winner(board)`**: Determines if there is a winner.
- **`terminal(board)`**: Checks if the game is over (either someone has won, or all spaces are filled).
- **`utility(board)`**: Returns a value based on the game's outcome (1 if X wins, -1 if O wins, 0 for a tie).
- **`minimax(board)`**: Implements the Minimax algorithm to find the optimal move for the current player.

---
