def compute(x, y, z):
    num1= x* (25/100)
    num2= y* (25/100)
    num3= z* (50/100)
    ans=num1 + num2 + num3
    return(ans)

hw_Average=float(input("Please enter your HW Average:"))
midterm=float(input("Please enter your midterm mark:"))
final=float(input("Please enter your final mark:"))


note=compute(hw_Average, midterm, final)
print("Your final grade is:", note)
