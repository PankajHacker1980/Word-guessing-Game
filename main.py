import random

def choose_word():
    words = ["apple", "banana", "cherry", "orange", "grape", "pear", "kiwi", "melon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def word_guessing_game():
    print("Welcome to the Word Guessing Game!")
    print("Try to guess the secret word.")

    secret_word = choose_word()
    guessed_letters = set()
    attempts_left = 7

    while attempts_left > 0:
        print("\n" + display_word(secret_word, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        
        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in secret_word:
                guessed_letters.add(guess)
                print("Correct guess!")
            else:
                print("Incorrect guess.")
                attempts_left -= 1
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                print(f"Congratulations! You guessed the word '{secret_word}' correctly!")
                break
            else:
                print("Incorrect guess.")
                attempts_left -= 1
        else:
            print("Invalid input. Please enter a single letter or the whole word.")

    if attempts_left == 0:
        print(f"\nSorry, you ran out of attempts. The word was '{secret_word}'.")

if __name__ == "__main__":
    word_guessing_game()
