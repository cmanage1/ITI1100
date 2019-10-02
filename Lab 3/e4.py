
def calculate (a, b ,c):
    disc= (b**2) - (4*a*c)
    return disc

a=float(input('Please enter a value for a:'))
b=float(input('Please enter a value for b:'))
c=float(input('Please enter a value for c:'))

ans=calculate(a, b, c)
if ans < 0:
    print("No real roots")
if ans == 0:
    print("One real root")
if ans >0:
    print("Two distinct real roots")
#Does not provide the right answer because the answer is close to\
#but not exactly 0
