def performTest(operation):
    ## complete your work here ##
    import random
    correctCounts=0

    for i in range (10):
        num1= random.randint(1,9)
        num2= random.randint(1,9)

        if operation == 0:
            print('\n',num1," + ", num2)
            user_ans=int(input("Please enter your answer:"))
            if user_ans == (num1+num2):
                print("Correct!")
                correctCounts+= 1
            else:
                print("Incorrect, the correct answer is ", num1+num2)

        elif operation == 1:
            print('\n',num1," * ", num2)
            user_ans=int(input("Please enter your answer:"))
            if user_ans == (num1*num2):
                correctCounts+= 1
                print("Correct!")
            else:
                print("Incorrect, the correct answer is ", num1*num2)
    return correctCounts

print("This software tests you with 10 questions …… ");
operation = int(input("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1): "))

correctCounts = performTest(operation)
print("\nYou have gotten ",correctCounts, " questions correct")
if correctCounts <= 6 :
  print("Please ask your teacher for help.")
else:
  print("Congratulations!")
