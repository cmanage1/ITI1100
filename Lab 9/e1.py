import random

def find(v, arr):
    Nsteps = 0
    for i in arr:
        Nsteps += 1
        if i == v:
            return(Nsteps , True)

    return (Nsteps , False)

v = int(input("Enter an integer: "))

N= 100
l3 = []
for i in range(N):
    num = random.randrange(N+1)
    l3.append(num)


ans = find(v,l3)
print("Number of steps:", ans[0] )
print(ans[1] )
