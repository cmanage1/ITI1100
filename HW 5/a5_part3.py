'''def star(n):
    print("*" * n)
    if n > 1:
        star(n - 1)
    print("*" * n)

n= 4
star(n)
'''


def sumListPos_rec(list , n , count = 0):
    if list[n-1] > 0:
        count+= list[n-1]
    if n == 0:
        return count
    else:
        return sumListPos_rec(list, n-1, count)

l = [1, -2, 5, 0, -5]

print ( sumListPos_rec( l , len(l)) )
