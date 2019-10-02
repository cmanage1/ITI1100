import math
repeat = True


def computeFact(n):
    for i in range(1, n):
        n*= i
    return n

while (repeat == True):
    n=int(input("Please enter a non-negative number:"))

    if n > 0:
        print("The factorial is:", computeFact(n))
        break
    elif n == 0:
        print(0)
        break
    else:
        print("Please enter a positive number")
