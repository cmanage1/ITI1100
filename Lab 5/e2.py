def compute(list):
    list.sort()
    n= 0
    for i in list:
        n+= i
    output = [ n/(len(list)), list[0], list[-1] ]
    print(output)

ch=input("Please enter a list of numbers seperated my commas:")
compute(list(eval(ch)))
