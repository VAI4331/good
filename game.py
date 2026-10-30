"""Simple text-based Hangman game."""

import random


WORDS = (
    "python",
    "computer",
    "programming",
    "keyboard",
    "internet",
    "elephant",
    "rainbow",
)
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = (
    """
     +---+
     |   |
         |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =======
    """,
)


def display_word(word, guessed_letters):
    """Show guessed letters and underscores for letters not yet guessed."""
    return " ".join(
        letter if letter in guessed_letters else "_" for letter in word
    )


def play_round():
    """Play one round and return whether the player won."""
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses remaining: {MAX_WRONG_GUESSES - wrong_guesses}")
        print(
            "Guessed letters: "
            + (", ".join(sorted(guessed_letters)) or "none")
        )

        guess = input("Guess one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print(f"\nYou win! The word was '{word}'.")
                return True
        else:
            wrong_guesses += 1
            print("That letter is not in the word.")

    print(HANGMAN_STAGES[MAX_WRONG_GUESSES])
    print(f"\nGame over! The word was '{word}'.")
    return False


def main():
    print("Welcome to Hangman!")
    print("Guess the hidden word one letter at a time.")

    while True:
        play_round()
        answer = input("\nPlay again? (yes/no): ").strip().lower()
        if answer not in {"yes", "y"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
