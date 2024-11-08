'''
import random

# Read the word bank from a file
with open("word_bank.txt", "r") as file:
    word_bank = file.read().splitlines()

# Choose a random word
current_word = random.choice(word_bank)

# Initialize game state
attempts = 5
game_over = False

# Game loop
while not game_over:
    # Get player's guess
    guess = input("Enter your guess: ").lower()

    # Check if the guess is correct
    if guess == current_word:
        print("Congratulations! You guessed the word.")
        game_over = True
    else:
        attempts -= 1
        if attempts == 0:
            print("Sorry, you ran out of attempts. The word was:", current_word)
            game_over = True
        else:
            print("Incorrect. You have", attempts, "attempts left.")
'''

import random

# Read the word bank from a file
with open("word_bank.txt", "r") as file:
    word_bank = file.read().splitlines()

# Choose a random word
current_word = random.choice(word_bank)

# Initialize game state
attempts = 5
game_over = False
guessed_letters = set()

'''
# Function to provide a hint
def get_hint(word):
    available_letters = set(word) - guessed_letters
    if available_letters:
        hint = random.choice(list(available_letters))
        guessed_letters.add(hint)
        return hint
    else:
        return None
'''

def get_hint(word):
    hint = word[:2]  # Get the first two letters
    return hint

# Game loop
while not game_over:
    # Get player's guess or hint request
    guess = input("Enter your guess (or 'hint' for a hint): ").lower()

    # Check if the guess is correct
    if guess == current_word:
        print("Congratulations! You guessed the word.")
        game_over = True
    elif guess == "hint":
        hint = get_hint(current_word)
        if hint:
            print("Hint:", hint)
        else:
            print("No more hints available.")
    else:
        attempts -= 1
        if attempts == 0:
            print("Sorry, you ran out of attempts. The word was:", current_word)
            game_over = True
        else:
            print("Incorrect. You have", attempts, "attempts left.")
