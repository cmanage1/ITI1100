def isDivisible(DATA):
    count=0
    if (DATA % 2 == 0) and (DATA % 3 == 0):
        return 1
    elif (DATA % 2 == 0) or (DATA % 3 == 0):
        return 2
    else:
        return 0


DATA=int(input("Please enter an integer:"))
num= isDivisible(DATA)
print(num)
