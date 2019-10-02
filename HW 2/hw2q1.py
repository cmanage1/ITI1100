def bmi(p, t):
    ## complete your work here ##
    r= (p / (t**2))
    ## return something for now
    return r

def print_bmi_level(r):
    ## complete your work here ##
    if r < 18.5:
        print (' underweight')
    elif 18 <= r < 25:
        print (' normal weight')
    elif 25 <= r < 30:
        print ('overweight')
    else:
        print (' obese')

p = float(input("Enter your weight in kilograms "))
t = float(input("Enter your height in meters "))

r = bmi(p,t)
print("Your BMI is", r)
print_bmi_level(r)
