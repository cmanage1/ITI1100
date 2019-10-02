import random

def doTest(operation):
    ## complete your work here ##
    num1= random.randint(1,9)
    num2= random.randint(1,9)

    if operation == 0:
        print('\n',num1," + ", num2)
        user_ans=int(input("Please enter your answer:"))
        if user_ans == (num1+num2):
            print("Correct!")
            return True
        else:
            print("Incorrect, the correct answer is ", num1+num2)

    elif operation == 1:
        print('\n',num1," * ", num2)
        user_ans=int(input("Please enter your answer:"))
        if user_ans == (num1*num2):
            print("Correct!")
            return True
        else:
            print("Incorrect, the correct answer is ", num1*num2)


responsesCorrect = 0
print("The software will process a test with 10 questions …… ")
for i in range (10):
    operation = random.randint(0,1)
    if doTest(operation) == True:
         responsesCorrect += 1

print(responsesCorrect, "Correct responses")
if responsesCorrect  <= 6 :
  print("Ask some help from your instructor.")
else:
  print("Congratulations!")
