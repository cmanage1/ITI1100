def histo_n(x):

    letters= {}
    for i in x:
        letters[i]= letters.get(i, 0) + 1

    letters= list(letters.items())
    letters.sort()
    return dict(letters) #IDK why the -3 is in the end in the example
                        #since -3 is less than 1????

raw_input=input("Please enter a list of numbers: ").strip().split()

input= tuple ([int(i) for i in raw_input])

print(histo_n(input))
