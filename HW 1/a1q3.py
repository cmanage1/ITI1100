#a1q3

def calculate(money):
    quarters= (money // 0.25)
    money-= (0.25*quarters)
    money=round(money, 2) #if no round the ans will not be correct

    dimes= money // 0.1
    money-= (0.1 *dimes)
    money=round(money, 2)

    nickels= money // 0.05
    money-= (0.05*nickels)
    money=round(money, 2)

    pennies= money //0.01

    totcoins= int(quarters + dimes + nickels + pennies)
    return totcoins


money=float(input("Enter the amount you are owed in $:"))
coins=calculate(money)
print("The minimum number of coins the cashier can return is:", coins)
