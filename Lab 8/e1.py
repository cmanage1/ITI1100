#return [[ matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def transpose(matrix):
    result= []
    for i in range (len(matrix[0])): # go through columns
        result.append([])
        for j in range(len(matrix)): # go through rows
            temp = matrix[j][i]
            result[i].append(temp)
    return result

'''
m = int(input("Enter the numbers of rows:"))
matrix = []
for i in range(m):
    print("Enter the row", i, "(spaces seperated by spaces)")
    row = [int(val) for val in input().strip().split()]
    matrix.append(row)
'''

matrix = [ [1,2,3] , [4,5,6]]

print(transpose(matrix))
