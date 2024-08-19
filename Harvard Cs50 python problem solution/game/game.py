#importing module
import random

keep_asking = True
while keep_asking:
    try:
        level = int(input("Enter the level: "))
        system_guess = random.randint(1, level)
        user_guess = int(input("Guess the number: "))

        if ( system_guess < user_guess ):
            print("Too large!")

        elif ( system_guess > user_guess ):
            print("Too small!")

        elif (system_guess == user_guess):
            print("Just right!")
            keep_asking = False

    except ValueError:
        continue
