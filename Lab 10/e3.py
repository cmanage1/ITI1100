class BankAccount:
    def __init__(self, name = 'Dupont', balance = 1000): #constructor
        self.name = name
        self.balance = balance
    def deposit(self, sum ):
        self.balance += sum
    def withdraw(self, sum):
        self.balance -= sum
    def display(self):
        print("The balance of " +self.name+" account is " +str(self.balance)+ " dollars")
    def __eq__(self, other):
        return self.name == other.name\
            and self.balance == other.balance
    def __repr__(self):
        return "The balance of "+self.name+" is "+str(self.balance)+" dollars"

if __name__ == "__main__":
    account1 = BankAccount('Duchmol' , 800)
    account1.deposit(350)
    account1.withdraw(200)
    account1.display()
    account2=BankAccount()
    account2.deposit(25)
    account2.display()

class AccountSaving(BankAccount):
    def __init__(self, name, balance, interest = 0.3):
        super().__init__(name, balance)
        self.interest= interest
    def changeRate(self, value):
        self.interest = value
    def capitalization(self, numberMonth):
        print("Capitalization on " +str(numberMonth)+" months at the monthly rate of "+str(self.interest)+"%")
        p = self.balance*((1+(self.interest/100))**numberMonth-1)
        self.balance+=p

if __name__ == "__main__":
    c1 = AccountSaving("Smith" , 600)
    c1.deposit(350)
    c1.display()
    c1.capitalization(12)
    c1.display()
    c1.changeRate(.5)
    c1.capitalization(12)
    c1.display()
