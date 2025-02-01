again = "yes"

while again == "yes":
    secret_word = "mosiah"
    guess_count = 0
    guess = ""

    print(f"\nYour hint is: {len(secret_word) * "_"}")

    while guess != secret_word:
        if guess_count <= 4:
            guess = input("What is your guess? ").lower()
            guess_count += 1
            
            if len(guess) != len(secret_word):
                print("Your guess must be the same length as the secret word!")
                continue
        
            hint = ""
            
            for i in range(len(secret_word)):
                if guess[i] == secret_word[i]:
                    hint += guess[i].upper()
                elif guess[i] in secret_word:
                    hint += guess[i].lower()
                else:
                    hint += "_"  
            
            if guess != secret_word:
                print(f"Your hint is: {hint}")
        
        else:
            print("Sorry, you didn't guessed before 5 attempts.\nGood Luck next time!")
            break

    print()
    print(f"Congratulations! You guessed!")
    print(f"It took you {guess_count} guesses.")
    
    print()
    again = str(input("Do you want to play again? (yes/no)\n")).lower()
    if again == "no":
        print("\nThanks for playing")
        
