DATA=int(input("Please enter an age:"))

if DATA >=18 and DATA <=55:
    good_age= True
    print("Transaction accepted")

else:
    good_age= False
    print("Transaction refused")
