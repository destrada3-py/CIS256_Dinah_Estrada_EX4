# guess_the_word.py

import random

# The following consists of a predefined list of science-related terms.

WORDS = ["Uranium", "Thorium", "Plutonium", "Enzyme", "Protein", "Cell", "Atom", "Molecule", "Acid", "Ion"]

def choose_word():
    """Retrieves a random word from the given list."""
    return random.choice(WORDS)

def display_progress(word, guessed_letters):
    # Returns a string displaying guessed letters and underscores representing unguessed characters.
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def play_game():
    # The following consists of the main game loop.
    print("--------------------------------------------------")
    print("🧪 Welcome to the Science Word Guessing Game!🧪")
    print("Guess the hidden science term one letter at a time!\n")
    print("--------------------------------------------------")

    secret_word = choose_word()
    guessed_letters = set()
    attempts_left = 10

    while attempts_left > 0:
        print(f"Hidden Term: {display_progress(secret_word, guessed_letters)}")
        print(f"Attempts Left: {attempts_left}")

        # ✅ Added: inner loop to keep asking until valid input is provided
        while True:
            guess = input("Guess a Letter: ").lower()

            # The following consists of validation to ensure the input 
            # meets required criteria.
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid Entry! Please enter only one letter (A-Z).\n")
                continue  # ask again
            if guess in guessed_letters:
                print("You have already selected that letter. Please choose a different one.\n")
                continue  # ask again
            break  # valid input received

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct!✅\n")
        else:
            print("Incorrect guess!\n")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations!🎉 You successfully identified the word: {secret_word}")
            break
    else:
        print(f"All attempts exhausted!🙅 The correct word was: {secret_word}")

if __name__ == "__main__":
    play_game()
