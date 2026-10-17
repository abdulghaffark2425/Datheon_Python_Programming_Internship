# Task 1: Hangman Game (Console)

A beginner-friendly, text-based Hangman game written in Python. The computer selects a word at random and the player guesses one letter at a time.

## Features

- Random word selection from a built-in word list
- Six incorrect guesses allowed
- Input validation (one alphabetic letter at a time)
- Prevents repeated guesses
- Win/lose messages and replay option
- Uses only Python's standard library

## Requirements

- Python 3.9 or newer recommended
- No third-party packages required

## Run the game

1. Download or clone this repository.
2. Open a terminal in this folder.
3. Run:

```bash
python hangman.py
```

On some systems, use `python3 hangman.py`.

## How to play

Type one letter and press Enter. Correct guesses reveal letters in the word. Guess the full word before you run out of incorrect guesses.

## Project structure

```text
Task_1_Hangman_Game/
├── hangman.py
└── README.md
```

## Learning outcomes

- Loops and conditionals
- Strings and sets
- Functions and input validation
- Random selection
- Basic program design

## Note

This is a learning project. The word list is stored in the source code and can be expanded by editing `WORDS` in `hangman.py`.
