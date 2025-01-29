from random import randint
def play():
    magic_number = randint(1, 100) 
    guessing = 0
    tries = 0

    while guessing != magic_number:
        guessing = int(input("What is your guess? "))
        tries += 1

        if guessing > magic_number:
            print("Lower")

        elif guessing < magic_number:
            print("Higher")

        elif guessing == magic_number:
            print("\nYou Guessed!")
            break
    print(f"Attempts: {tries}")

play()

while True:
    again = str(input("Play Again?\n Yes or No")).lower()
    if again == "yes":
        play()

    elif again == "no":
        print("Game Over!")
        break
    else:
        print(again)
    
