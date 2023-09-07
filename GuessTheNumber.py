import random
import os
import art

EASY_LEVEL = 10
HARD_LEVEL = 5

def checkGuess(answer, guess):
    if answer == guess:
        print(f"Congatulations you got it!")
        return 100
    elif answer > guess and answer - guess <= 5:
        print("Ow! You are so close. Aim higher!")
        return 101
    elif answer > guess:
        print("Too low. Aim higher")
        return 101
    elif answer < guess and guess - answer <= 5:
        print("Ah! You are so close. Aim lower!")
        return 101
    elif answer < guess:
        print("Too high! Aim a bit lower")
        return 101
    else: 
        return 102

keepPlaying = True
while keepPlaying:
    print(art.logo)
    answer = random.randint(1,100)
    print(f"Welcome to Number Guesser. \nI have selected a number between 1 and 100")
    modeSelected = input("Select from the modes available: \nEasy \nHard\n").lower()
    if modeSelected == "easy":
        chance = EASY_LEVEL
    else:
        chance = HARD_LEVEL
    print(f"You have selected {modeSelected.upper()} mode. You have {chance} tries")

    for i in range(0, chance):
        guess = int(input("Enter the number you think I have guessed \n"))
        if checkGuess(answer=answer, guess=guess) == 100:
            break
        else:
            print("Try again, ")
            chance = chance - 1
            print(f"Tries left {chance}\n")
            if chance == 0:
                print(f"Uh ho! You are out of tries! The answer was {answer}")

    playAgain = input("Do you want to play again? y for yes and n for no\n").lower()
    if playAgain == "n":
        keepPlaying = False
    else:
        os.system("cls")