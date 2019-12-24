def product_matrices(m1, m2):
    result = []
    for i in range (len(m1)): #go through rows of m1
        result.append([])
        for j in range (len(m2[0])): #go through columns of m2
            temp= 0
            for k in range (len(m2)): #go through rows of m1 again
                temp += m1[i][k]*m2[k][j]
            result[i].append(temp)
        print(result)

    return result

m1= [[1,2,3] , [4,5,6]]
m2= [[1,2] , [3,4] , [5,6]]


print(product_matrices(m1, m2))
