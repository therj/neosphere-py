import random

randomNum = random.randint(1, 20)
print(randomNum)  # To guess
userGuess = None
# '' will work but it is a blank string, it's not nothing. It is a string.
# None is actually Nothing, much like null.
# type(None) is NoneType

while userGuess is not randomNum:
    userGuess = input("Guess the number beweeen 1 & 20: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("\nYou're supposed to enter a number!\n")
print("You guessed it correct!")

# TODO: 1. Print how many times the user guessed before getting it correct
# TODO 2  Limit the number of tries to 10
# TODO 3. Show success/fail message for above case!
