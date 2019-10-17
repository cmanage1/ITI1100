def count_pos(num):
    count=0
    for i in num:
        if i > 0:
            count+=1
    return count

raw_input=input("Please input a list of numbers separated by spaces: ").strip().split()
input= [float(i) for i in raw_input] #convert str to int for each element

print("There are", count_pos(input) ,"positive numbers in your list")
