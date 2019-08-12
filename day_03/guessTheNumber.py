import random

randomNum = random.randint(1, 20)
print(randomNum)  # To guess
userGuess = None
while userGuess is not randomNum:
    print("Try your luck!")
    userGuess = int(input("Guess the number beweeen 1 & 20: "))


print("You guessed it correct!")
