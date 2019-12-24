#return [ [ m1[i][j] + m2[i][j] for j in range(len(m1))] for i in range (len(m1[0]))]

def sum_matrix(m1, m2):
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range (len(m2[0])):
            temp = m1[i][j] + m2[i][j]
            result[i].append(temp)

    return result

matrix1= [ [ 1,2] , [3,4]]
matrix2= [ [ 1,1] , [1,1]]

print(sum_matrix(matrix1 , matrix2))
