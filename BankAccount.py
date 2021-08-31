class BankAccount:
    balance = 0
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
    
    def makeDeposit(self, amount):
        self.balance += amount
        return self
    
    def makeWithdrawal(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Your balance is: " + str(self.balance))
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self


Jake = BankAccount(0.01, 100)
Jake.makeDeposit(100).makeDeposit(100).makeDeposit(100).makeWithdrawal(100).yield_interest().display_account_info()

print("-------------------------------------------------------------")

John= BankAccount(0.02, 200)
John.makeDeposit(200).makeDeposit(200).makeWithdrawal(100).makeWithdrawal(100).makeWithdrawal(100).makeWithdrawal(100).yield_interest().display_account_info()
