#Pythagorean pair program

def pythagorean_pair(a, b):
    c=((a**2)+(b**2)) ** (1/2)
    return ((c % int(c)) == 0) #checking mod to see if there's no remainder

a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))

#I can print this from the function but function needed a 'return" so..
check=pythagorean_pair(a,b)
