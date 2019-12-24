def find_m(M , num):
    Nsteps = 0
    for i in M:
        for j in i:
            Nsteps +=1
            if j == num:
                return (Nsteps, True)

    return (Nsteps , False)


M = [ [1,2,10] , [7,5,6] , [8,8,9,10] ]
print (M)
num = int(input("Enter the value you want to search: "))

ans = find_m(M, num)

print("Number of steps :", ans[0])
print(ans[1])
