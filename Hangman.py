import random

# List of words to choose from
words = ['python', 'hangman', 'programming', 'computer', 'artificial']

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        display = display_word(word, guessed_letters)
        print(f"Word: {display}")
        print(f"Attempts left: {attempts}")
        
        if '_' not in display:
            print("Congratulations! You guessed the word.")
            break
        
        if attempts == 0:
            print(f"Game over! The word was '{word}'.")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")
        else:
            print("Correct guess!")

if __name__ == "__main__":
    print("Welcome to Hangman!")
    hangman()
