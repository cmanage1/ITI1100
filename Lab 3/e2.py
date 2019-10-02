DATA= int(input("Please enter a temperature:"))

if DATA >= 80:
    print("Swimming")
elif (DATA >= 60) and (DATA <80):
    print("Soccer")
elif (DATA >= 40) and (DATA <60):
    print("Volleyball")
else:
    print("Skying")
