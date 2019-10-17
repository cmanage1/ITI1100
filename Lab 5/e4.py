
def calculate(list):
    a=s=0
    for i in range ( len(list)):
        a+= list[i]
    a = a / len(list) #Mean is correct

    for x in range ( len(list)):
        s+= (list[x]- a)**2

    s=s/(len(list))
    print(s**(1/2))

ch= input(("Please enter a list of numbers:"))
calculate(list(eval(ch)))
