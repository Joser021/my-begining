print("welcome to the Word Guessing Game!")

word = "mosiah"
guess = ""
total_guess = 0

while word != guess:
    print()
    guess = str(input("What is your guess? " )).lower()
    total_guess += 1

    if guess == word:
        print("Congratulations! You Guessed it!")
    
    else:
        print("Your guess was not correct.")
print(f"Total Guesses: {total_guess}")
