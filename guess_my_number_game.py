play_again = "yes"
print()
while play_again == "yes":

    from random import randint

    magic_number = randint(1, 100)
    guess = -1
    guess_count = 0

    while magic_number != guess:
        guess = int(input("What is your guess? "))
        guess_count += 1

        if guess == magic_number:
            print("You did it! Congrats!!")

        elif guess > magic_number:
            print("Lower")

        else:
            print("Higher")

    print(f"Guesses: {guess_count}")
    print()

    play_again = str(input("Do you want to play again? (Yes or No)\n")).lower()
    if play_again == "yes":
        print()
        print("NEW GAME")
    else:
        print("Thanks for playing!")
