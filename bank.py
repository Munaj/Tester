class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self,amount):
        self.balance += amount

    def witchdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry not enough funds!")

    def statement(self):
        print(f"Account Balance: ${self.balance}")

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance =-1000)

    def __str__(self):
        return f"{self.name}'s Current Account Ballance: {self.balance}"

class Saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance =0)

    def __str__(self):
        return f"{self.name}'s Saving Account Ballance: ${self.balance}"


Z = Current("Jakub", 500)
Z.deposit(300)
Z.witchdraw(1900)
T = Saving("Jakubus", 300)
print(T)
print(Z.statement())
print(Z)
