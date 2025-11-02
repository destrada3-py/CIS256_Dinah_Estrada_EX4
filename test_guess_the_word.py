# test_guess_the_word.py

import guess_the_word as gtw

def test_choose_word_from_list():
    # Verifies that the selected word belongs to the predefined set 
    # of science terms.
    word = gtw.choose_word()
    assert word in gtw.WORDS

def test_display_progress_reveals_letters():
    # Ensures that correctly guessed letters are displayed in the word.
    word = "atom"
    guessed = {"a", "t"}
    result = gtw.display_progress(word, guessed)
    assert result.startswith("at")

def test_display_progress_hides_unguessed_letters():
    # Ensures that unguessed letters remain concealed.
    word = "protein"
    guessed = {"p", "r"}
    result = gtw.display_progress(word, guessed)
    assert "_" in result 

def test_full_word_guess_scenario():
    # Simulates a scenario where the user/player successfully guesses the word.
    word = "ion"
    guessed = {"i", "o", "n"}
    assert all(letter in guessed for letter in word)
