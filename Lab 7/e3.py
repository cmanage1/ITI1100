def sum_of_three(x):
    print(len(x))
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            for k in range(j+1, len(x)):
                if x[i] + x[j] + x[k] == 0:
                    return True
    return False

raw_input= input("Please enter a list of numbers seperated by spaces: ").strip().split()
input = tuple ( [ int(i) for i in raw_input ] )

print(sum_of_three(input))
