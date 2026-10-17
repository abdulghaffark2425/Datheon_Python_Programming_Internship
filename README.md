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
---

# Task 2: Stock Portfolio Tracker

A terminal-based stock portfolio manager written in Python. It helps users manage a simple investment portfolio with real-time price calculations using hardcoded stock values.

## Features
- Pre-defined dictionary of real-time stock prices (AAPL, TSLA, MSFT, GOOGL, AMZN, NVDA)
- Input validation for stock symbols and positive share quantities
- Dynamic summary table generation with individual stock values
- Automatic total investment portfolio calculation
- Pure Python implementation with zero external dependencies

## Run Task 2
```bash
python stock_tracker.py

---

## Task 3: Automated File Organizer & Cleanup Utility

An automated Python utility that cleans up cluttered directories by sorting files into categorized folders based on their file extensions.

### Features
* Categorizes files into `Documents`, `Images`, `Videos`, `Archives`, and `Code`.
* Automatically creates destination category folders if they do not exist.
* Handles file naming collisions seamlessly to prevent overwriting existing files.
* Includes exception handling for permission and filesystem errors.
* Displays a detailed execution summary showing total relocated files.
---

## Task 4: Rule-Based Interactive Terminal Assistant / Chatbot

A responsive, rule-based customer support assistant that processes user inputs using regular expressions and keyword matching to provide contextual responses based on an FAQ dataset.

### Features
* **Dataset Driven:** Dynamic responses loaded directly from `sample_faq.json`[cite: 8].
* **Intent Recognition:** Uses keyword score matching and regular expressions to identify user intents[cite: 8].
* **Input Normalization:** Strips extra spaces and converts input to lowercase for robust pattern matching[cite: 8].
* **Graceful Fallbacks:** Handles low-confidence or unrecognized queries with helpful fallback suggestions[cite: 8].
* **Clean Session Termination:** Allows users to exit gracefully using `'exit'`, `'quit'`, or `'bye'` commands[cite: 8].

### How to Run Task 4
```bash
python chatbot.py
