def insertionSort(l):
    for i in range (1, len(l)):
        current = l[i]
        position = i

        while position>0 and l[position-1] > current:
            l[position] = l[position -1 ]
            position -=1

        l[position] = current

    return l

x = input("Enter the list space by space: ").strip().split()
numbers = [ int(i) for i in x]

print(numbers)
print( insertionSort(numbers) )
