"""Console Hangman game for the Datheon Python internship."""

import random

WORDS = [
    "python", "github", "internship", "programming", "computer",
    "portfolio", "automation", "developer", "keyboard", "function",
]
MAX_WRONG_GUESSES = 6


def display_word(word: str, guessed_letters: set[str]) -> str:
    """Return the word with unguessed letters hidden."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game() -> None:
    """Run one round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters: set[str] = set()
    wrong_letters: set[str] = set()

    print("\n=== HANGMAN GAME ===")
    print(f"Guess the word! You can make {MAX_WRONG_GUESSES} incorrect guesses.")

    while len(wrong_letters) < MAX_WRONG_GUESSES:
        print("\nWord:", display_word(word, guessed_letters))
        if wrong_letters:
            print("Incorrect guesses:", ", ".join(sorted(wrong_letters)))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - len(wrong_letters)}")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            return

        guess = input("Enter one letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue
        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter. Try another one.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            wrong_letters.add(guess)
            print("Sorry, that letter is not in the word.")

    print(f"\nGame over! The word was: {word}")


def main() -> None:
    """Offer replay until the player quits."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
