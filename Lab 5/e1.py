def compute(list):
    avg= 0
    for i in list:
        avg+= i
    print( (avg/ (len(list))) )

ch=input("Please enter a list of numbers seperated my commas:")
compute(list(eval(ch)))
