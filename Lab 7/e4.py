def move_zeros_v1(list):
    temp = []
    new_list= []
    for i in list:
        if i == 0:
            temp.append(i)
        else:
            new_list.append(i)
    return new_list + temp

def move_zeros_v2(list):
    for j in x:
        if j == 0:
            x.append(x.pop(x.index(j)))

def move_zeros_v3(x):
    for i in range (len(x)):
        for j in range (i+1, len(x)):
            if x[i] == 0 and x[j] != 0:
                temp = x[i]
                x[i]= x[j]
                x[j] = temp

raw_input= input("Enter a list of numbers seperated by spaces: ").strip().split()
input = [int(i) for i in raw_input]

#print(input, move_zeros_v1(input))
#print(input, move_zeros_v2(input))
print(input, move_zeros_v3(input))
