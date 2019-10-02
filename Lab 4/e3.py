import random

def guess_algo( x):

    for i in range(1,100):
        guess=int(input("\nPlease enter a guess between 1 and 10...:"))

        if guess == x:
            print("Congrats you have guessed the number in", i, "tries")
            break

        elif guess < x:
            print("Try #",i,": You are guessing too low")

        elif guess > x:
            print("Try #",i,": You are guessing too high")

x=random.randint(1,10)
guess_algo(x)
