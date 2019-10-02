import math

def computeArea(side1, side2, side3):
    p=side1 + side2 + side3
    ans= (math.sqrt(p* (p - 2*side1) * (p-2*side2) * (p-2*side3)))/4
    return (ans)


side1=int(input("Enter the length of slide 1:"))
side2=int(input("Enter the length of slide 2:"))
side3=int(input("Enter the length of slide 3:"))

area= computeArea(side1, side2, side3)

print("The area of the triange is:", area)
