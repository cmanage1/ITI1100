def two_length_run(num):
    for i in range (len(num)-1):
        for x in range (i+1, len(num)):
            if num[x] == num[i]:
                return True
    return False

raw_input=input("Please input a list of numbers separated by spaces:").strip().split()
input= [float(i) for i in raw_input] #convert str to int for each element

print(two_length_run(input))
