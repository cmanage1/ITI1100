import random

def count(l3, N):
    Nstep = 0
    counter = 0

    for i in l3:
        Nstep += 1
        if i == l3:
            counter +=1

    return Nstep

N= 100
l3 = []
for i in range(N):
    num = random.randrange(N+1)
    l3.append(num)

N = int(input("Enter a number you want to search:"))

print("Number of steps:", count(l3, N))
