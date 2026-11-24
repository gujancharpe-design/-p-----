import random

# 1. Small list of 5 predefined words
words = ["python", "coding", "laptop", "screen", "window"]

# Pick a random word from the list
secret_word = random.choice(words)

# Create a list of underscores to represent unguessed letters
display_word = ["_"] * len(secret_word)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("You have", max_incorrect, "incorrect guesses allowed.")

# 2. Main game loop
while incorrect_guesses < max_incorrect and "_" in display_word:
    print("\nCurrent word:", " ".join(display_word))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)
    
    guess = input("Guess a single letter: ").lower()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue
        
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue
        
    guessed_letters.append(guess)
    
    # 3. Check if the guessed letter is in the secret word
    if guess in secret_word:
        print("Good job! '" + guess + "' is in the word.")
        # Reveal the matched letter(s)
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display_word[index] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess! '" + guess + "' is not in the word.")

# 4. End of game result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame Over! You ran out of guesses. The word was:", secret_word)