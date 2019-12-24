def add(x):
    for i in range (len(x)):
        for j in range (len(x[0])):
            x[i][j] +=1

def add_V2(x):
    result = []
    for i in range (len(x)):
        result.append([])
        for j in range (len(x[0])):
            result[i].append(x[i][j]+1)
    return result
#---------------------------------------------------------------
print("Input the array elements with spaceds between columns.\
\nOne row per line, and an empty line at the end")

arr = []
while True:
    line= input()
    if not line: break
    values = line.split()
    temp = [ int(val) for val in values]
    arr.append(temp)

print("The array is:\n",arr)

add(arr)
print("After executing the function add, the array is:\n", arr )

new_arr = add_V2(arr)

print("A new array is created with add_V2:\n", new_arr)

print("After executing the function add_V2, the initial array is:\n", arr )
