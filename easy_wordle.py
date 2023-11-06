#Nathan Solomon
import random
from words import words
from wordle import check_word, known_word, no_letters, yes_letters

def filter_word_list(words, clues):
    # Function to filter the list of possible words based on the provided clues
    possible_words = []
    for candidate_word in words:
        candidate_word_upper = candidate_word.upper()
        # Check if the candidate word is consistent with all provided clues
        is_candidate_valid = all(check_word(candidate_word_upper, guess) == expected_clues for guess, expected_clues in clues)
        if is_candidate_valid:
            possible_words.append(candidate_word_upper.lower())
    return possible_words




def easy_game(secret):
    # Function defining the easy level of the game
    guesses = []

    for _ in range(6):
        print(f"\nWords possible: {len(words)}")

        user_guess = input("> ").upper()
        while user_guess not in words or len(user_guess) != 5:
            print("Not a word or not of length 5. Try again")
            user_guess = input("> ").upper()

        clues = check_word(secret, user_guess)
        guesses.append((user_guess, clues))

        possible_words = filter_word_list(words, guesses)
        random.shuffle(possible_words)
        # Display a subset of possible words to the player
        display_words = possible_words[:min(5, len(possible_words))]
        print(f"\nPossible words: {display_words}")

        if "green" * 5 in clues:
            print(f"\nCongratulations! You guessed the word: {secret}")
            break
        elif _ == 5:
            print(f"\nSorry! Out of guesses. The word was: {secret}")

if __name__ == "__main__":
    secret_word = random.choice(words)
    easy_game(secret_word)
