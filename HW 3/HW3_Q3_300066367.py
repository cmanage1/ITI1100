'''
def longest_run(num):
    #this function has error for input= None
    counter= [None] * ( len(num) -1 ) #makes arr with (empty) elements

    for i in range (0, len(num)-1):
        counter[i] = num.count(num[i]) #adds count of each num to an arr

    counter.sort(reverse=True) #sort arr backwards (biggest to smallest)
    return counter[0] #return the first (biggest) element
'''

def longest_run(num):
    old_counter= 0
    for i in range (0, len(num)):
        new_counter=1
        for x in range (i+1, len(num)):
            if num[x] == num[i]: #code upto here is same as before
                new_counter += 1
        if new_counter > old_counter: #if this count > old loop count
            old_counter= new_counter  #make this the old loop count

    return old_counter #return the biggest count

raw_input= input("Please input a list of numbers seperated by spaces:").strip().split()
input= [int(i) for i in raw_input] #change type str to int for each element

print(longest_run(input))
